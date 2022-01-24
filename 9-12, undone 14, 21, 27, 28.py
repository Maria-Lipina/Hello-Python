import random

def digits (n):
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10
    return digits #Не забывать, что цифры записываются в список справа-налево!

# a = random.randrange(100, 1000)

# print(f'{a} - число в задачах 9 - 10, 12')

# digits_a = digits(a)

# print(digits_a)


# print("9. Показать последнюю цифру трёхзначного числа")

# print(digits_a[2])


# print("10.Показать вторую цифру трёхзначного числа")

# print(digits_a[1])


# print("11.Дано число из отрезка [10, 99]. Показать наибольшую цифру числа")

# b = random.randrange(10, 100)

# digits_b = digits(b)

# if digits_b[0] > digits_b[1]:
#     print(f'{b} --> {digits_b[0]}')
# else: print(f'{b} --> {digits_b[1]}') 


# print("12.Удалить вторую цифру трёхзначного числа")

# print(f'{a} --> {digits_a[2] * 10 + digits_a[0]}')


# print("14.Найти третью цифру числа или сообщить, что её нет")

c = 678901

# digits_c = digits(c)

# if len(digits_c) > 2:
#     print(digits_c[2])
# else: print(None)

print("21.Программа проверяет пятизначное число на палиндромом.")


def is_palindrome(arg):
    l_arg = digits(arg)
    rng = (len(l_arg) // 2)
    print(f'для цикла: {rng}')
    for i in range(0, rng, +1):
        for j in range(len(l_arg), rng, -1):
            print(f'{i} --- {j}')
            # print (f'{i} - {l_arg[i]}')
            # print (f'{j} - {l_arg[j]}') вычесть из длины i
        if l_arg[i] != l_arg[-i]: return False
#         else: return True

print(f'{c} - {is_palindrome(c)}')

print("27.Определить количество цифр в числе")

print("28.Подсчитать сумму цифр в числе")
