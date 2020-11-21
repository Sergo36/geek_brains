f_o = open("Task2.txt", "r")
str = f_o.readline()
cnt = 0
while str != "":
    cnt += 1
    print(F"В {cnt} строке {len(str.split(' '))} слов")
    str = f_o.readline()
print(F"Количество строк в файле {cnt}")
f_o.close()
