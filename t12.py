print('12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.\n Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}')

def sequence(n):
    return {n: n*3+1 for n in range(1, n+1)}

print(sequence(6))