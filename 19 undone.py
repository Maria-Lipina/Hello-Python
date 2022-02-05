import datetime
from re import X
import statistics

print("19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел")

# asifseed = str(datetime.datetime.now())
seed = '2022-02-05 11:24:08.668276'
#Нужно получить "[20, 22, 02, 05, 11, 24, 08, 66, 82, 76] - сделать метод
seed = [20, 22, 2, 5, 11, 24, 8, 66, 82, 76]

m = max(seed) 
print(m)
a = int(statistics.mean(seed))
print(a)
c = min(seed)
print(c)

# n = m только итератор для понимания, сколько сисел необходимо сделать

def linear(m, a, c, n):
    while n != 0:
        x = int((a * linear(m, a, c, n) + c) % m)
        print (x)

linear(m, a, c, m)