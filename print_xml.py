# encoding: utf-8

import lxml
from lxml import etree, objectify


def print_element(file_name, name_contain):
    tree = lxml.etree.parse(file_name)
    res = tree.xpath('/resources')[0]  # 获取bndbox元素的内容
    had_print = False
    max_text_len = 0
    for ss in res.getchildren():  # 便利bndbox元素下的子元素
        element_name = ss.get("name")
        if str(element_name).__contains__(name_contain):
            element_text = ss.text
            element_text_len = len(element_text)
            if element_text_len > 35:
                if not had_print:
                    print file_name
                    had_print = True
                print element_name
                print element_text_len
                max_text_len = max_text_len if max_text_len > element_text_len else element_text_len
    if max_text_len != 0:
        print "max _signup_title_ = " + str(max_text_len)


if __name__ == "__main__":
    print "__main__"
    prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
    file_name = "res/values-fr/strings.xml"
    name_contain = "_signup_title_"
    print_element(file_name, name_contain)
