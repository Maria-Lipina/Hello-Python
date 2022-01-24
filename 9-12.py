import random

def digits (n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return digits #Не забывать, что цифры записываются в список справа-налево!

a = random.randrange(100, 1000)

print(f'{a} - число в задачах 9 - 10, 12')

digits_0 = digits(a)

print(digits_0)

print("9. Показать последнюю цифру трёхзначного числа")

print(digits_0[2])

print("10.Показать вторую цифру трёхзначного числа")

print(digits_0[1])

print("11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа")

b = random.randrange(10, 100)

digits_1 = digits(b)

if digits_1[0] > digits_1[1]:
    print(f'{b} --> {digits_1[0]}')
else: print(f'{b} --> {digits_1[1]}') 

print("12.Удалить вторую цифру трёхзначного числа")

print(f'{a} --> {digits_0[2] * 10 + digits_0[0]}') 
