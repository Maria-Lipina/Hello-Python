print('11. Для натурального N создать список из N членов последовательности: \nДля N = 5: 1, -3, 9, -27, 81 и т.д.')

def g_prog(b, q, n):
    return [b*((q)**(i)) for i in range(n)]

print(g_prog(1, -3, 5))