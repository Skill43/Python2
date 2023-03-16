# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.

def sum(a, b):
    if b == 0:
        return a
    else: 
        return sum(a+1, b-1) 
a = int(input("Ведите число a: "))
b = int(input("Ведите число b: "))
res = sum(a, b)
print("Сумма чисел", a, "и", b, "=", res)
