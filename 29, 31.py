print("29. Найти НОК двух чисел")

import timeit #TODO разобраться с модулем тайминга и аргументами к нему
from prime_test import prime # https://pypi.org/project/prime-test/ - ссылка на внешнюю библиотеку
from math import gcd, lcm

def prime_factor(num: int):
    res = {}
    while num > 1:
        if prime.test(num):
            res |= {num: 1}
            return res
        else:
            divide = 2
            while num > 1:
                if not (num % divide):
                    if divide in res: 
                        res[divide] += 1
                        num = num // divide
                    else: 
                        res |= {divide: 1}
                        num = num // divide
                else: divide +=1
    return res

def LCM (n: int, m: int):
    a = prime_factor(n)
    b = prime_factor(m)
    c = a | b
    d = list(a.keys() & b.keys())
    for i in d:
        if a[i] > b[i]: c[i] = a[i]

    e = list(c)
    lcm = 1
    for j in e:
        lcm = lcm * (j ** c[j])
    return lcm

def LCM2 (n: int, m: int):
    return abs((n * m)) // gcd(n , m)

def LCM3 (n: int, m: int):
    return lcm(n, m)

print(f'Первый способ {LCM(457230957, 572309570)}')
print(f'Второй способ {LCM2(457230957, 572309570)}')
print(f'Третий способ {LCM3(457230957, 572309570)}')


print("31. Составить список простых множителей натурального числа N")
print(list(prime_factor(457230957)))
