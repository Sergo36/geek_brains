f_o = open("Task3.txt", "r")
lst = f_o.readlines()
f_o.close()
sumSal = 0
for el in lst:
    fam, sal = el.split(' ')
    intSal = int(sal)
    sumSal += intSal
    if intSal < 20000:
        print(fam)
print("Средняя зарплата", sumSal / len(lst))
