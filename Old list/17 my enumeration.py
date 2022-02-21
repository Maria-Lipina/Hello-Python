print("Cформировать случайным образом целочисленный массив A из натуральных двузначных чисел")

import random
import statistics

def fill_ints(length, min, max):
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

li_a = fill_ints(20, 0, 100)

print("Создать на его основе масcив B, отбрасывая те числа, которые в массиве А нарушают порядок возрастания")

def ascend_filter(li:list):
    res = [li[0]]
    compare = li[0]
    for i in range(1, len(li)):
        if li[i] > compare: 
            res.append(li[i])
            compare = li[i]
    return res

li_b = ascend_filter(li_a) #можно ли сделать это с помощью list comprehension и mapping?

print("Создать на его основе масcив С, отбрасывая те числа, которые в массиве А четные")

li_c = [i for i in li_a if i%2]

print("Создать на его основе масcив D, отбрасывая те числа, которые больше среднего арифметического элементов A")

li_d = [i for i in li_a if i < statistics.mean(li_a)]