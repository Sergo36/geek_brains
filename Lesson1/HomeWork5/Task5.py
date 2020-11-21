from random import randint

list = [str(randint(0, 99)) + '\n' for x in range(0, 100)]
f_o = open("Task5.txt", "w")
f_o.writelines(list)
f_o.close()

f_o = open("Task5.txt", "r")
list = f_o.readlines()
f_o.close()

listint = [int(x) for x in list]
print(sum(listint))
