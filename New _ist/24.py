print("24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19")
import math
import randomizer as rdm

source = rdm.fill_reals(10, 0, 10)
fractions = [round(source[i] - math.floor(source[i]), 3) for i in range(len(source))]
print(max(fractions)-min(fractions))