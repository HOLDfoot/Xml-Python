# encoding: utf-8

import lxml
from lxml import etree, objectify

tree = lxml.etree.parse("text.xml")
# get bbox
for bbox in tree.xpath('//bndbox'):   # 获取bndbox元素的内容
    for corner in bbox.getchildren():  # 便利bndbox元素下的子元素
        print corner.text   # string类型