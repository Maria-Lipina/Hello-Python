from json.encoder import INFINITY

print("9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти")

def coordinates(quarter):
    if quarter == 1: return f'X - 0:{INFINITY}. Y - 0:{INFINITY}'
    elif quarter == 2: return f'X - {-INFINITY}:0. Y - 0:{INFINITY}'
    elif quarter == 3: return f'X - {-INFINITY}:0. Y - {-INFINITY}:0'
    elif quarter == 4: return f'X - 0:{INFINITY}. Y - {-INFINITY}:0'

print(
    coordinates(
        int(input())
        ))
