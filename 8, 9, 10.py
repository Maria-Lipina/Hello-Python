
import math
from json.encoder import INFINITY
import randomizer as rdm

def quarter (dot):
    if dot [0] == 0: return 'ось X'
    if dot [1] == 0: return 'ось Y'
    if dot[0] > 0:
        if dot[1] > 0: return 1
        else: return 4
    elif dot[1] > 0: return 2
    else: return 3

def coordinates(quarter):
    if quarter == 1: return f'X - 0:{INFINITY}. Y - 0:{INFINITY}'
    elif quarter == 2: return f'X - {-INFINITY}:0. Y - 0:{INFINITY}'
    elif quarter == 3: return f'X - {-INFINITY}:0. Y - {-INFINITY}:0'
    elif quarter == 4: return f'X - 0:{INFINITY}. Y - {-INFINITY}:0'

def distance (dot1, dot2):
    xx = (dot2[0] - dot1[0])**2
    yy = (dot2[1] - dot1[1])**2
    return math.sqrt(xx - yy) #почему, если вся формула в одну строчку - ValueError: math domain error?

print("8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У ")

dot1 = rdm.fill_list(2, -20, 21)
print(dot1)
print(quarter(dot1))


print("9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти")

print(coordinates(quarter(dot1)))


print("10. Найти расстояние между двумя точками пространства")

dot2 = rdm.fill_list(2, -20, 21)
print(dot1)
print(dot2)

print(distance(dot1, dot2))