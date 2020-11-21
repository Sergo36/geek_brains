f_o = open("Task1.txt", "w")
str = input("Введите строку: ")
while str != "":
    f_o.write(str + "\n")
    str = input("Введите строку: ")
f_o.close()
