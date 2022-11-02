print("21. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.")
"""Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1"""


def second_position(item, source: list):
    if source.count(item) > 1:
        for i in range(source.index(item)+1, len(source)):
            if source[i] == item:
                return i


with open('t21in.txt', 'r', encoding='utf-8') as input:
    li_in = input.readlines()

print(second_position('Когда теряет равновесие\n', li_in))
