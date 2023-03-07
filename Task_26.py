# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def to_pow(a, b):
    if b < 1:
        return 1
    return a * (to_pow(a, b - 1))


print(to_pow(int(input('Input A: ')), int(input('Input B: '))))