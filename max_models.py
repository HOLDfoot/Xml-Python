# encoding=utf-8

class MaxModel(str):

    def __new__(cls, value, *args, **keywargs):
        return str.__new__(cls, value)

    def __init__(self,file_name,max_len):
        #self.file_name = file_name
        #self.max_len = max_len
        self.out = "(" + file_name + "," + str(max_len) + ")"

    def __str__(self):
        return self.out