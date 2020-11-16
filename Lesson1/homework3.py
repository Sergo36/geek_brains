######### task 1
print("task 1 " + "*"*50)
def division(numerator, denominator):
    if denominator == 0:
        print("Деление на ноль")
        return
    else:
        return numerator/denominator
numerator = int(input("Введите числитель: "))
denominator = int(input("Введите знаменатель: "))
print(division(numerator, denominator))

######### task 2
print("task 2 " + "*"*50)
def myPrint(firstName = "", lastName = "", year = 1900, city = "", email = "", tel = ""):
    return F"Hello {lastName} {firstName} {year} {city} {email} {tel}"

param = {
    "tel": "8 800 555 3535",
    "firstName": "Sergey",
    "lastName" : "Repin",
    "year": 1996,
    "city": "Voronezh",
    "email": "example@mail.ru"

}
print(myPrint(**param))

######## task 3
print("task 3 " + "*"*50)
def my_func(num1, num2, num3):
    list = [num1, num2, num3]
    list.sort(reverse=True)
    return sum(list[:2])
num1 = int(input("Введите чило 1: "))
num2 = int(input("Введите число 2: "))
num3 = int(input("Введите число 3: "))
print(my_func(num1, num2, num3))

######### task 4
print("task 4 " + "*"*50)
def power1(x, y):
    return 1/(x**(y*-1))

def power2(x, y):
    res = 1
    while y < 0:
        res = res * x
        y += 1
    return 1/res

x = int(input("Введите чило: "))
y = int(input("Введите отрицательную степень: "))

print(power1(x, y))
print(power2(x, y))

######### task 5
print("task 5 " + "*"*50)
def mySum(summ, var=""):
    list = var.split(" ")
    for elem in list:
        if elem == ".":
            return summ
        elif elem == "":
            continue
        else:
            summ += int(elem)
    return summ


str = ""
summ = 0
while str.count(".") == 0:
    str = input("Введите числа разделенные пробелом: ")
    summ = mySum(summ, str)

print(summ)

######### task 6
print("task 6 " + "*"*50)

def int_func(str):
    return chr(ord(str[:1]) - 32) + str[1:]  # Я помню про capitalize()
                                             # И да, тут надо бы проверять что символ в латинском диапазоне, но чет лень
                                             # Тем более в задании сказано что ничего кроме латиницы на вход не будет подоваться

str = input("Введите строку: ")
print(int_func(str))

Bigstr = input("Введите большую строку: ")
list = Bigstr.split(" ")
i = 0
while i < len(list):
    list[i] = int_func(list[i])
    i += 1
print(" ".join(list))
