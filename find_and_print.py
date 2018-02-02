# encoding=UTF-8

import sys
import find_strings_file as find_file
import print_xml as print_element

prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
flamingo_tuple = ("flamingo",)
friendsfinder_tuple = ("friendsfinder",)
getfriends_tuple = ("getfriends",)
kkfriendstuple = ("kkfriends",)

if len(sys.argv) >= 2:
    print_detail = int(sys.argv[1])
else:
    print_detail = 1

name_contain = "feedback"
mini_bounds = 18

print name_contain + "在以下文件中长度应该小于" + str(mini_bounds)
finded_files = find_file.get_finded_file()
for file in finded_files:
    #print file
    print_element.print_element(file, name_contain, mini_bounds, print_detail)
# print print_element.max_list
# print print_element.all_max