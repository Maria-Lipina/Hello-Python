import random

print("17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число")

def sum_on_positions(li: list, positions_file: str):
    res = 1
    with open(positions_file, 'r') as file:
        positions = map(int, file.read().split())
        for i in positions:
            res *= li[i]
    return res

n = 10
li = [random.randrange(-n, n+1) for i in range(n)]
print(li)
print(sum_on_positions(li, "17.txt"))

