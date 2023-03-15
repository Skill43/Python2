# Найдите сумму цифр трехзначного числа.

def get_num():
    while True:
        try:
            num = int(input("Введите трехзначное число: "))
            if len(str(num)) == 3:
                return num
            else : (print("Ошибка! Попробуйте еще раз!"))
        except ValueError:
            print("Вы ввели не число. Попробуйте ещё раз.")
num = get_num()
sum_num = num // 100 + (num // 10) % 10 + num % 10
print("Сумма цифр трехзначного числа =", sum_num)