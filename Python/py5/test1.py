#   Напишите программу, которая на вход принимает два числа A и B, 
#   и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return power(A, B//2) * power(A, B//2)
    else:
        return A * power(A, B//2) * power(A, B//2)
A = int(input("Ведите число А: "))
B = int(input("Ведите число В: "))
res = power(A, B)
print(A, "в степени", B, "=", res)