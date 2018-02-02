# encoding: utf-8

import lxml
from lxml import etree, objectify
from max_models import MaxModel

max_list = []
global all_max
all_max = 0

def print_element(file_name, name_contain, mini_bounds=35, print_detail=1):
    tree = lxml.etree.parse(file_name)
    res = tree.xpath('/resources')[0]  # 获取bndbox元素的内容
    had_print = False
    max_text_len = 0
    for ss in res.getchildren():  # 便利bndbox元素下的子元素
        element_name = ss.get("name")
        if str(element_name).__contains__(name_contain):
            element_text = ss.text
            element_text_len = len(element_text)
            if element_text_len >= mini_bounds:
                if not had_print:
                    print file_name[5:len(file_name)]
                    had_print = True
                if print_detail != 0:
                    print element_name + "长度:" + str(element_text_len)
                    #print element_text_len
    #             max_text_len = max_text_len if max_text_len > element_text_len else element_text_len
    # if max_text_len != 0:
    #     # print "max _signup_title_ = " + str(max_text_len)
    #     file_name = file_name[5:len(file_name)]
    #     max_model =  "(" + file_name + "," + str(max_text_len) + ")"
    #     max_list.append(max_model)
    #     global all_max
    #     all_max = all_max if all_max > max_text_len else max_text_len



if __name__ == "__main__":
    print "__main__"
    prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
    file_name = "res/values-fr/strings.xml"
    name_contain = "_signup_title_"
    print_element(file_name, name_contain)
