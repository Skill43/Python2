# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

a = input("Введите элементы массива A через пробел: ")
array = a.split()
for i in range(len(array)):
    array[i] = int(array[i])
b = input("Введите элементы массива B через пробел: ")
array1 = b.split()
for i in range(len(array1)):
    array1[i] = int(array1[i])

res = list(set(array + array1))
res.sort()
print("Уникальные числа множеств A и B:", res)