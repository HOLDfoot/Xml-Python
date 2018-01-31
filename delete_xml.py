# encoding: utf-8

import lxml
from lxml import etree, objectify

tree = lxml.etree.parse("strings.xml")

def prn_obj(obj):
    print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])

res = tree.xpath('/resources')[0]   # 获取bndbox元素的内容
for ss in res.getchildren():  # 便利bndbox元素下的子元素
    #print ss.text   # string类型
    #prn_obj(ss)
    name = ss.get("name")
    if str(name).__contains__("getfriends"):
        print name
        res.remove(ss)
#etree.ElementTree(tree.ElementTree()).write("strings.xml", pretty_print=True)
#print tree

tree.write("strings.xml")
