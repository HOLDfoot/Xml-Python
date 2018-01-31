# encoding=UTF-8

import find_strings_file as find_file
import delete_xml as delete_element

prefix_tuple = ("flamingo", "friendsfinder", "getfriends", "kkfriends")
flamingo_tuple = ("flamingo")
friendsfinder_tuple = ("friendsfinder")
getfriends_tuple = ("getfriends")
kkfriendstuple = ("kkfriends")

finded_files = find_file.get_finded_file()
for file in finded_files:
    print file
    delete_element.delete_element(file, prefix_tuple, True)