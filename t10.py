from t8 import random_dot
from math import sqrt

print("10. Найти расстояние между двумя точками пространства")

def distance (dot1, dot2):
    xx = (dot2[0] - dot1[0])**2
    yy = (dot2[1] - dot1[1])**2
    return sqrt(xx + yy)

dot1 = random_dot(30)
dot2 = random_dot(30)
print(distance(dot1, dot2))