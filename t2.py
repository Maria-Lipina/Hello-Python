# Найти максимальное из пяти чисел

import random

def do():
    a = [random.randint(0, 1000) for i in range(5)]
    print(a)
    return max(a)

print(do())