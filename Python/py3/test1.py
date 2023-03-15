# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

n = input("Введите элементы массива через пробел: ")
array = n.split()
for i in range(len(array)):
    array[i] = int(array[i])
x =int(input("Ведите число: "))
count = 0 
for element in array:
    if element == x:
        count += 1
print("Массив: ", array)
print("Число", x, "встречается в массиве", count, "раз(а).")