# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.

n = input("Введите элементы массива через пробел: ")
array = n.split()
for i in range(len(array)):
    array[i] = int(array[i])
x =float(input("Ведите число: "))
min_num = abs(array[0] - x)
for element in array:
    num = abs(element - x)
    if num < min_num:
        min_num = num
        res = element
print("Массив: ", array)
print("Самый близкий по величине элемент в массиве к числу", x, ":", res)