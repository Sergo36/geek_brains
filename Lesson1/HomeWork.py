######### task 1
print("task 1 " + "*"*50)
var1 = 1
var2 = "a"
var3 = "123"
var4 = True
var5 = 1.5
print(var1, var2, var3, var4, var5)
print(type(var1), type(var2), type(var3), type(var4), type(var5))
#myfirstvar = input("Введите число ")
myfirstvar = 123

print("Вы ввели '{}' это переменная типа {}".format(myfirstvar, type(myfirstvar)))
myfirstvar = int(myfirstvar)
print("После магии введенное вами значение '{}' преобразовалось к типу {}".format(myfirstvar, type(myfirstvar)))

######### task 2
print("task 2 " + "*"*50)
#usersek = int(input("Введите время в секундах "))
usersek = 1024
hours = usersek // 3600
minutes = (usersek - hours * 3600) // 60
seconds = usersek - hours * 3600 - minutes * 60

res = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
print(res)

######### task 3
print("task 3 " + "*"*50)
#num = (input("Введите число "))
num = "3"
num2 = int("%s%s" % (num, num))
num3 = int("%s%s%s" % (num, num, num))
res = int(num) + num2 + num3
print(res)

######### task 4
print("task 4 " + "*"*50)
#num = int(input("Введите число "))
num = 123321
maximum = 0

while num > 0:
    currentNum = num % 10
    if currentNum > maximum:
        maximum = currentNum
    num //= 10
print(maximum)

######### task 5
print("task 5 " + "*"*50)
#income = int(input("Введите выручку ")) #Будем считать что выручка и издержки целочисленные
income = 100
#consumption = int(input("Введите издержки ")) #Учет ведем в попугаях
consumption = 5
if income > consumption:
    print("Фирма работает с прибылью")
    profit = income - consumption
    print("Рентабельность %f" % (profit/income))
    #numberEmployees = int(input("Введите количество сотрудников "))
    numberEmployees = 3
    print("Прибыль фирмы %f попугаев в расчете на одного сотрудника " % (profit / numberEmployees))
elif income < consumption:
    print("Фирма работает с убытком")
else:
    print("Фирма работает в ноль")

######### task 6
print("task 6 " + "*"*50)
#a = int(input("Введите начальный результат спортсмена"))
a = 2
#b = int(input("Введите желаемый результат спортсмена"))
b = 3
countDay = 1
# вариант раз
#while a <= b: #Вроде не менее это не строгое неравенство
#    print("{}-й день {:2.2f}".format(countDay, a))
#    a = a + a * 0.1
#    countDay += 1
#print("{}-й день {:2.2f}".format(countDay, a))

# вариант два если страшно когда вывода два
# и очень хочется вывод результатов в цикле
# иммитация do while
while True:
    print("{}-й день {:2.2f}".format(countDay, a))
    if a > b: # в это варианте неравенство строгое
        break
    a = a + a * 0.1
    countDay += 1

print("Ответ: на {}-й день спортсмен достиг результата — не менее {} км.".format(countDay, b))
