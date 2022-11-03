from random import randrange

print("23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.") 
"""Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]"""

input = [randrange(-10, 11) for i in range(5)]
res = [input[i] * input[-1-i] for i in range(round(len(input) / 2))]
print(res)