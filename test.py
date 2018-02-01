# encoding=utf-8

from max_models import MaxModel


max = MaxModel("file", 44)

max_list = [max, max, max]

print max
print "[" + ",".join(max_list) + "]"
