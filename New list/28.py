print("28.Найти корни квадратного уравнения Ax² + Bx + C = 0: \n1) Математикой")

import math

def quadratic_equation(a, b, c):
    if a == 0: return 'invalid coefficient a'
    elif b == 0:
        if (-c)/a < 0: return 'no equation root'
        else: return [-(math.sqrt((-c)/a)), math.sqrt((-c)/a)]
    elif c == 0: return [0, (-b)/a]
    elif c == 0 and b == 0: return 0
    else:
        D = b**2 - 4*a*c
        if D < 0: return 'no equation root'
        if D == 0: return (-b)/2*a
        if D > 0: return [(
                           ((-b) - math.sqrt(D))/(2*a)
                           ), 
                           (
                            ((-b) + math.sqrt(D))/(2*a)
                          )]

print(quadratic_equation(5, 3, -1))

print("2) Используя дополнительные библиотеки*")