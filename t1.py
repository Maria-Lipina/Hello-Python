# По двум заданным числам проверить является ли одно квадратом второго
# TODO: убрать get_input из самого метода

import view as v

def do():
    a = int(v.get_input())
    b = int(v.get_input())
    return a == b**2
