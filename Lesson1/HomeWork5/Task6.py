from re import sub
data = []
f_o = open("Task6.txt", "r")
str = f_o.readline()
while str != "":
    data.append(str.split(' '))
    str = f_o.readline()
f_o.close()


Schedule = {}
for lesson in data:
    sum = 0
    for i in range(1, len(lesson)):
        hStr = sub(r'[^0-9.]+', r'', lesson[i])
        hInt = 0 if hStr == "" else int(hStr)
        sum += hInt
    Schedule[lesson[0].replace(":", "")] = sum
print(Schedule)

