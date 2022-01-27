import random
print("6. Выяснить является ли число чётным")

a = random.randrange(100)
is_even = not a % 2
print(f'четность {a} - {is_even}')


print("8.Показать четные числа от 1 до N")

n = random.randrange(100)
print(list(range(0, n+1, 2)))