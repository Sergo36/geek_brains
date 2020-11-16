import random
import time
######### task 1
print("task 1 " + "*"*50)
list = [1, 1.2, "str", True, [1, 2, 3], (1, 2, 3), {"firstname": "sergey", "lastname": "repin"}]
for elem in list:
    print(type(elem))

######### task 2
print("task 2 " + "*"*50)
list = []
for i in range(10):
    list.append(random.randint(0, 10))
print(list)

startTime = time.time()
for i in range(0, len(list) - 1, 2):
    list[i], list[i + 1] = list[i + 1], list[i]
endTime = time.time()
print(list)
print(endTime - startTime) # этот вариант оказался быстрее

startTime = time.time()
for i in range(0, len(list) - 1, 2):
    temp = list[i]
    list[i] = list[i + 1]
    list[i + 1] = temp
endTime = time.time()
print(list)
print(endTime - startTime)

######### task 3
print("task 3 " + "*"*50)

list1 = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
list2 = ["Зима", "Весна", "Лето", "Осень"]
dict1 = {1: "Зима",
         2: "Зима",
         3: "Весна",
         4: "Весна",
         5: "Весна",
         6: "Лето",
         7: "Лето",
         8: "Лето",
         9: "Осень",
         10: "Осень",
         11: "Осень",
         12: "Зима"}
dict2 = {0: "Зима",
         1: "Весна",
         2: "Лето",
         3: "Осень"}

# numberMonth = int(input("Введите номер месяца: "))
numberMonth = 1

option1 = numberMonth - 1
option2 = (numberMonth // 3) % 4
print(list1[option1])
print(list2[option2])
print(dict1[numberMonth])
print(dict2[option2])

######### task 4
print("task 4 " + "*"*50)
str = "My first string 0123456789999"
list = str.split()
cnt = 1
for elem in list:
    print(cnt, elem[:10])
    cnt += 1

######### task 5
print("task 5 " + "*"*50)
list = [7, 5, 3, 3, 2]
list.sort(reverse=True) # сортируем первоначальный лист с рейтингом на случай не корректного ввода

number = 3
fl = False
for i in range(len(list) - 1, -1, -1):
    if list[i] >= number:
        list.insert(i + 1, number)
        fl = True
        break
if not fl:
    list.insert(0, number)

number = 5
fl = False
cnt = len(list)
for i in list[::-1]: # очень захотелось прикрутить срез
    if i >= number:
        list.insert(cnt, number)
        fl = True
        break
    cnt -= 1
if not fl:
    list.insert(0, number)
print(list)

######### task 6
print("task 5 " + "*"*50)
print("Для выхода введите '.'")
list = []
cnt = 1
while True:
    options = {"Наименование": None,
               "Цена": None,
               "Количество": None,
               "ед": None}
    name = input("Введите наименование товара: ")
    if name == ".": break
    options["Наименование"] = name

    cost = input("Введите цену товара: ")
    if cost == ".": break
    options["Цена"] = int(cost)

    count = input("Введите количество товара: ")
    if count == ".": break
    options["Количество"] = int(count)

    ed = input("Введите единицы измерения товара: ")
    if ed == ".": break
    options["ед"] = ed
    list.append((cnt, options))
    cnt += 1

print(list)

analytics = {"Наименование": [],
             "Цена": [],
             "Количество": [],
             "ед": []}
for elem in list:
    sl = elem[1] # Раз у нас неизменяемый кортеж обращусь здесь по индексу))
    for key in sl.keys():
        if analytics[key].count(sl[key]) == 0:
            analytics[key].append(sl[key])

print(analytics)
