import random

print('14. Подсчитать сумму цифр в вещественном числе.')


def digits(n):
    n = int(str(n).replace('.', ''))
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return digits


n = random.uniform(0, 100)
print(n)
print(sum(digits(n)))
