#!/usr/bin/env python3
import lxml
import elementpath
import markdown
from lxml.html import etree, fromstring
import numpy as np
import sys
from copy import deepcopy

# -----------------------------------------------------------------------------
def dprint(*args):
    print(*args)
# careful not to mix debug print with file output to stdout
dprint = lambda *x: None

# -----------------------------------------------------------------------------
def lxml_inner_html(elem, encoding='utf-8'):
    return lxml.etree.tostring(elem, pretty_print=True).decode(encoding)

def clone_elem(elem):
    return fromstring(lxml_inner_html(elem))

def md_to_doc(mdstr, no_p=True):
    doc = fromstring(markdown.markdown(mdstr))
    if no_p:
        return doc.xpath("*")[0]
    else:
        return doc

def tuple_array(lst, n=2):
    return np.array(lst, dtype=object).reshape(-1,n)

def pair_dict(lst):
    return dict(tuple_array(lst, 2))

import re
h_all = re.compile(r"[hH]\d")
h_1 = re.compile(r"[hH]1")
def h_level(level=None):
    if level is None:
        return h_all
    if level == 1:
        return h_1
    else:
        return re.compile(r"[hH][1-"+f"{level}]")

def filter_to_hn(elems, skip=1, level=None):
    """For a list of Elements truncate as soon as a heading is encoutered, 
       ignore and keep the first `skip` headings. If `level` is given, do 
       not stop at deeper heading levels.
       """
    hn = h_level(level)
    for el in elems:
        if hn.match(el.tag):
            if not skip:
                break
            skip -= 1
        yield el

# ----------------------------------------------------------------------------
# begin of main function

strin = sys.stdin.read()
doc = fromstring(strin)

# obtain all h2 headings that follow h1 Categories
cat_headings = tuple_array(elementpath.select(doc, "//h1[text()='Categories']/following-sibling::h2/(a/@id,.)"))

# obtain all h2 headings that follow h1 Lessons
#lesson_headings = pair_dict(elementpath.select(doc, "//h1[text()='Lesson Index']/following-sibling::h2/(a/@id,.)"))
lesson_headings = tuple_array(elementpath.select(doc, "//h1[a/@id='lessons']/following-sibling::h2/(a/@id,.)"))

# for each heading, find all terms that refer to its anchor
# add the terms as references under the category heading
# if the category heading is a lesson, do not add the terms

for tag, elem in cat_headings:
    cat_terms = tuple_array(elementpath.select(doc, f"(//a[@href='#{tag}']/preceding::h3[1]/(text(),@id,.))"), n=3)
    if tag not in lesson_headings[:,0]:
        dprint(tag)
        for (term, href, node) in cat_terms:
            refnode = md_to_doc(f"[{term}](#{href})<p>", no_p=True)
            elem.addnext(refnode)
            elem = refnode

# special processing of lesson categories
# instead of term reference, add full definition heading and body

for tag, elem in lesson_headings:
    # obtain all terms that refer to this lesson's anchor
    cat_term_sections = tuple_array(elementpath.select(doc, f"(//a[@href='#{tag}']/preceding::h3[1]/(text(),@id))"))
    dprint(len(cat_term_sections))
    dprint(tag)
    for term, href in cat_term_sections:
        # get all nodes related to the term, it's h3 and following sibling nodes up to next h1-3 [complicated]
        elems_after_term_h3 = elementpath.select(doc,f"//h3[text()='{term}']/(self::*,following-sibling::*)")
        section_nodes = list(filter_to_hn(elems_after_term_h3, level=3))
        for sn in section_nodes:
            sn = deepcopy(sn) # without clone the paragraph would disappear in its original location
            elem.addnext(sn)
            elem = sn

# print modified HTML doc to stdout
print(lxml_inner_html(doc))
