# encoding=UTF-8

import find_strings_file as find_file
import print_xml as print_element

prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
flamingo_tuple = ("flamingo",)
friendsfinder_tuple = ("friendsfinder",)
getfriends_tuple = ("getfriends",)
kkfriendstuple = ("kkfriends",)

name_contain = "_signup_title_"

finded_files = find_file.get_finded_file()
for file in finded_files:
    #print file
    print_element.print_element(file, name_contain)