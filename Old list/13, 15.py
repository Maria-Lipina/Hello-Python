import random

def isfold (a, b):
    if a % b == 0: return True
    else: return False

a = 966

print("13.Выяснить, кратно ли число заданному, если нет, вывести остаток.")

print(isfold(a, 5))

print("15.Дано число. Проверить кратно ли оно 7 и 23.")

print(isfold(a, 7) and isfold(a, 23))