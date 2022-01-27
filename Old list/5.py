import math

print("5.Написать программу вычисления значения функции y = f(a). \n Фактически - a* Sin(x)/x, как уточнил заказчик")

def f (x, a):
    return a * math.sin(math.radians(x)) / x

print(f(60, 5))
