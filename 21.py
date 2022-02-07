print("Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.")
"""Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1"""

source = ['ORz6', 'ORz6', '368G', 'GD4,oO5']
source1 = ['4no', 'A3s', '5vj', '4no', '5vj', 'x4n']

def positions (source, elem):
    pos = []
    for i in range(len(source)):
        if source[i] == elem:
            pos.append(i)
    return pos

poss = positions(source1, '4no')
if len(poss) >=2: print(poss[1])
else: print(-1)

