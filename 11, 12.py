n = 10

print('11. Для натурального N создать список из N членов последовательности: \nДля N = 5: 1, -3, 9, -27, 81 и т.д.')

def geom_prog(b, q, n):
    series = [b]
    for i in range(1, n):
        series.append(b*((q)**(i)))
    return series

print(geom_prog(1, -3, n))

print()
print('12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.\n Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}')

dictio = {n: n*3+1 for n in range(1, n+1)}
print (dictio)