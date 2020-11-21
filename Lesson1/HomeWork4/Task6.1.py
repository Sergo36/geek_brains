from sys import argv
from itertools import count
file_path, arg1, arg2 = argv
start = int(arg1)
finish = int(arg2)

for el in count(start):
    if el > finish:
        break
    else:
        print(el)