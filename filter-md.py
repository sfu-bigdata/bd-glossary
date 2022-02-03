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

def pair_dict(lst):
    return dict(np.array(lst, dtype=object).reshape(-1,2))

import re
hn = re.compile(r"[hH]\d")

def filter_to_hn(elems, skip=1):
    """For a list of Elements truncate as soon as a heading is encoutered, ignore and keep the first `skip` headings."""
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
cat_headings = pair_dict(elementpath.select(doc, "//h1[text()='Categories']/following-sibling::h2/(a/@id,.)"))

# for each heading, find all terms that refer to its anchor
# add the terms as references under the category heading

for tag, elem in cat_headings.items():
    cat_terms = pair_dict(elementpath.select(doc, f"(//a[@href='#{tag}']/preceding::h3[1]/(text(),@id))"))
    dprint(tag)
    for term, href in cat_terms.items():
        refnode = md_to_doc(f"[{term}](#{href})<p>", no_p=True)
        elem.addnext(refnode)
        elem = refnode

# obtain all h2 headings that follow h1 Lessons
lesson_headings = pair_dict(elementpath.select(doc, "//h1[text()='Lessons']/following-sibling::h2/(a/@id,.)"))

for tag, elem in lesson_headings.items():
    # obtain all terms that refer to this lesson's anchor
    cat_term_sections = pair_dict(elementpath.select(doc, f"(//a[@href='#{tag}']/preceding::h3[1]/(text(),@id))"))
    dprint(tag)
    for term, href in cat_term_sections.items():
        # get all nodes related to the term, it's h3 and following sibling nodes up to next h1-3 [complicated]
        section_nodes = list(filter_to_hn(elementpath.select(doc,f"//h3[text()='{term}']/(self::*,following-sibling::*)")))
        for sn in section_nodes:
            sn = deepcopy(sn) # without clone the paragraph would disappear in its original location
            elem.addnext(sn)
            elem = sn

# print modified HTML doc to stdout
print(lxml_inner_html(doc))
