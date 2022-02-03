print("16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму")

n = 7
li = list(map(lambda n: (1 + 1/n)**n, list(range(1, n))))
print(sum(li))