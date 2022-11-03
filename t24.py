from random import random
from math import floor

print(
    "24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19")


source = [round(random(), 3) for i in range(5)]
fractions = [round(i - floor(i), 3) for i in source]
print(source)
print(max(fractions)-min(fractions))