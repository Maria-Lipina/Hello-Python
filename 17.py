import random
print("17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число")

n = 10
li = [random.randrange(-n, n+1) for i in range(n)]
print(li)

file = open('17.txt', 'r')
a = int(file.read(1)) #index 3 Чем readline отличается от read?
b = int(file.read(2)) #index 7
print(li[a] * li[b])
file.close()