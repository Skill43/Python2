# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = input("Введите элементы массива через пробел: ")
array = n.split()
for i in range(len(array)):
    array[i] = int(array[i])
min_num = int(input("Введите начало диапазона: "))
max_num = int(input("Введите конец диапазона: "))
res = []
for i in range(len(array)):
    if min_num <= array[i] <= max_num:
        res.append(i)
print("Индексы элементов, принадлежащих диапазону от" , min_num ,"до",max_num,":", res)