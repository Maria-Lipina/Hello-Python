import csv
import random

print("19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел")
# https://ru.wikipedia.org/wiki/Линейный_конгруэнтный_метод


def linear(m, a, c, n=0):
    if n == 0:
        return (a + c) % m
    else:
        return (a * linear(m, a, c, n-1) + c) % m

for i in range(10):
    print(linear(11979, 859, 2531, i))
