#2. Даны два числа. Показать большее и меньшее число

import random

a = random.randint(1, 100)
b = random.randint(1, 100)

if a > b: print(f'max = {a}, min = {b}')
else: print(f'max = {b}, min = {a}')

#4. Даны два числа. Показать большее и меньшее число

list_a = [4, 9, 10]
max = list_a[0]
for i in list_a:
    if i > max:
        max = i
print(max)