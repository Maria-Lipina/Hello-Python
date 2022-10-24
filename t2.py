import random

print("2. Найти максимальное из пяти чисел")

def find_max(*args):
    return max(*args)

print(find_max(
    [random.randrange(-10, 11) for i in range(5)]
    ))