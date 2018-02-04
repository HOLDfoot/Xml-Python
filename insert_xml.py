# encoding: utf-8

import lxml
from lxml import etree, objectify

def add_element(file_name):
    tree = lxml.etree.parse(file_name)
    res = tree.xpath('/resources')[0]
    children = res.getchildren()
    count = len(children)
    print "count = %s" % count
    for ss in children:
        name = ss.get("name")
        print name
        index = res.index(ss)
        print "index = %s" % index
        ss.tail = "\n"

    E = objectify.ElementMaker(annotate=False)
    element = E.string("Zhang San")
    element.set("name", "person_name")
    element.tail = "\n"
    res.insert(count, element)

    tree.write(file_name, encoding='utf-8')

if __name__ == "__main__":
    print "__main__ test.py"
    file_name = "values-de/strings.xml"
    add_element(file_name)
