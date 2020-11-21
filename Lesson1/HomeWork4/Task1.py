from sys import argv

def salary(hours, rate, prize):
    return hours * rate + prize

file_path, arg1, arg2, arg3 = argv
print(salary(int(arg1), int(arg2), int(arg3)))
