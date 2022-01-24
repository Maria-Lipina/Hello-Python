#2. Даны два числа. Показать большее и меньшее число

import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if a > b: print(f'max = {a}, min = {b}')
else: print(f'max = {b}, min = {a}')

#4. Найти максимальное из трех чисел

list_a = [4, 9, 10]

print(max(list_a))