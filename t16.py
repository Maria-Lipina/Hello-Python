print("16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму")

def sequence (n):
    return [((1 + 1/i)**i) for i in range(1, n)]

print(sum(sequence(7)))