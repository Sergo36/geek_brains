def fact(n):
    currentNumber = 1
    while currentNumber <= n:
        res = 1
        i = currentNumber
        while i > 0:
            res *= i
            i -= 1
        currentNumber += 1
        yield res

for el in fact(30):
    print(el)
