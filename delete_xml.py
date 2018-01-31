# encoding: utf-8

import lxml
from lxml import etree, objectify

file_name = "values-de/strings.xml"
prefix = "kkfriends"

def delete_element(file_name, prefix_tuple, remove = False):
    tree = lxml.etree.parse(file_name)
    res = tree.xpath('/resources')[0]   # 获取bndbox元素的内容
    for ss in res.getchildren():  # 便利bndbox元素下的子元素
        name = ss.get("name")
        name_divided = str(name).split("_");
        is_contain = False
        if len(name_divided) > 1:
            name_prefix = name_divided[0]
            if prefix_tuple.__contains__(name_prefix):
                is_contain = True

        print "%s contains %s , name_prefix = %s" % (name, str(is_contain), name_prefix)
        if remove:
            if is_contain:
                res.remove(ss)
        else: # 保留这些标签
            if not is_contain:
                res.remove(ss)

    tree.write(file_name, encoding='utf-8')

prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
delete_element(file_name, prefix_tuple, True)
