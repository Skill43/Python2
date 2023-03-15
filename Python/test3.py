# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

def get_num():
    while True:
        try:
            num = int(input("Введите цифры с билета: "))
            if len(str(num)) % 2 == 0:
                return num
            else: (print("Ошибка! Этот билет не может быть счастливым! \nПопробуйте следующий!"))
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз.")
num = get_num()

num_digits = len(str(num))
half_digits = num_digits // 2
first_half = num // 10**(num_digits - half_digits)
second_half = num % 10**(num_digits - half_digits)

def digit_sum(number):
    return sum(int(n) for n in str(number))

first_sum = digit_sum(first_half)
second_sum = digit_sum(second_half)
if (first_sum == second_sum):
    print("Удача!! Это счастливый билет")
else : print("К сожалению, билет не счастливый.")