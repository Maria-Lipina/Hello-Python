import datetime
import statistics

print("19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел")

moment = str(datetime.datetime.now())
print(moment)
for i in moment:
    if i == '-' or i == ' ' or i == ':' or i == '.':
        moment = moment.replace(i, '')

pre_seed = []
for i in range(1, len(moment)+1):
    if not i % 2:
        pre_seed.append(int(moment[i-2:i]))

print(pre_seed)

def linear(m, a, c, d, n=0):
        if n == 0: return int((a * d + c) % m)
        else: return int((a * linear(m, a, c, n-1) + c) % m)

""" При вводных данных [20, 22, 2, 5, 11, 24, 8, 66, 82, 76] перечень случайных получается: 20, 29, 21, 0"""

m = max(pre_seed) #82
a = int(statistics.mean(pre_seed)) #31
c = min(pre_seed) #2
d = sum(pre_seed) % m #40
rdm = (a * d + c) % m #70

for i in range(10):
    print(linear(a, c, m, i))