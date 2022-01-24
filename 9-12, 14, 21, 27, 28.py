import random

def digits (n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return digits #Не забывать, что цифры записываются в список справа-налево!

a = random.randrange(100, 1000)
print(f'{a} - число в задачах 9 - 10, 12')
digits_a = digits(a)
print(digits_a)


print("9. Показать последнюю цифру трёхзначного числа")

print(digits_a[2])


print("10.Показать вторую цифру трёхзначного числа")

print(digits_a[1])


print("11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа")

b = random.randrange(10, 100)
digits_b = digits(b)
print(f'{b} --> {max(digits_b)}')


print("12.Удалить вторую цифру трёхзначного числа")

print(f'{a} --> {digits_a[2] * 10 + digits_a[0]}')


print("14.Найти третью цифру числа или сообщить, что её нет")

d = random.randrange(1_000)
print(f'{d} --> ')
digits_d = digits(d)
if len(digits_d) > 2:
    print(digits_d[2])
else: print(None)


print("21.Программа проверяет пятизначное число на палиндром.")

def is_palindrome(arg):
    l_arg = digits(arg)
    rng = (len(l_arg) // 2)
    for i in range(rng):
        if l_arg[i] != l_arg[len(l_arg)-1-i]: return False
    return True

c = 67876
digits_c = digits(c)
print(f'{c} - {is_palindrome(c)}')


print("27.Определить количество цифр в числе")

e = random.randrange(1_000_000_000_000)
print(f'{e} - число в задачах 27, 28')

digits_e = digits(e)
print(len(digits_e))


print("28.Подсчитать сумму цифр в числе")

print(sum(digits_e))