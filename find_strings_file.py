# encoding: utf-8
import os
import sys
import commands

def get_finded_file():
    reg_find = "find res/ -name strings.xml"
    tuple_find = commands.getstatusoutput(reg_find)
    #print tuple_find[1]
    string_files = tuple_find[1].split("\n")
    return string_files


