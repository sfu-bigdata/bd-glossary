#!/usr/bin/env python3
import lxml
import elementpath
import markdown
from lxml.html import etree, fromstring
import numpy as np
import sys

def lxml_inner_html(elem, encoding='utf-8'):
    return lxml.etree.tostring(elem, pretty_print=True).decode(encoding)

def md_to_doc(mdstr, no_p=True):
    doc = fromstring(markdown.markdown(mdstr))
    if no_p:
        return doc.xpath("*")[0]
    else:
        return doc

def pair_dict(lst):
    return dict(np.array(lst, dtype=object).reshape(-1,2))

strin = sys.stdin.read()
doc = fromstring(strin)

# obtain all h2 headings that follow h1 Categories
cat_headings = pair_dict(elementpath.select(doc, "//h1[text()='Categories']/following-sibling::h2/(a/@id,.)"))

# for each heading, find all terms that refer to its anchor
# add the terms as references under the category heading

for tag, elem in cat_headings.items():
    cat_terms = pair_dict(elementpath.select(doc, f"(//a[@href='#{tag}']/preceding::h3[1]/(text(),@id))"))
    print(tag)
    for term, href in cat_terms.items():
        refnode = md_to_doc(f"[{term}](#{href})<p>", no_p=True)
        elem.addnext(refnode)
        elem = refnode

# print modified HTML doc to stdout
print(lxml_inner_html(doc))
