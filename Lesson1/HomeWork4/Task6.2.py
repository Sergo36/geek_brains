from sys import argv
from itertools import cycle
file_path, arg1, arg2 = argv
lst = arg2.split(',')
finish = int(arg1) #Тут еще можно умножить на длину списка
# что бы выводить всю последовательность определенное кол-во раз
# по заданию не понятно ограничение на длину результата или итераций вывода исходной последовательности6
cnt = 0
for el in cycle(lst):
    if cnt > finish:
        break
    print(el)
    cnt += 1