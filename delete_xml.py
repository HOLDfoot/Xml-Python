# encoding: utf-8

import lxml
from lxml import etree, objectify

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

        # print "%s contains %s , name_prefix = %s" % (name, str(is_contain), name_prefix)
        if remove:
            if is_contain:
                res.remove(ss)
                print "delete element name = " + name
        else: # 保留这些标签
            if not is_contain:
                res.remove(ss)
        ss.tail = "\n"
    tree.write(file_name, encoding='utf-8')
    append_header(file_name)

def append_header(file_name):
    file_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    file_read = open(file_name, "r")
    file_body = file_read.read()
    file_read.close()
    file_write = open(file_name, "w")
    file_write.write(file_header + file_body)
    file_write.close()

if __name__ == "__main__":
    print "main"
    prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
    file_name = "values-de/strings.xml"
    delete_element(file_name, prefix_tuple, True)
