print("7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат")
"                                          2   1   1       3  6 4  6 5"

def logic (preds):
    x, y, z = preds[0], preds[1], preds[2]
    expression = not (x or y or z) == (not x and not y and not z)
    return expression

pred_head = ['x', 'y', 'z']
pred_value = [
    [True, True, True],
    [False, True, True],
    [True, False, True],
    [True, True, False],
    [True, False, False],
    [False, False, True],
    [False, True, False],
    [False, False, False],
]

print('x      y       z     -->  result')
for i in range(len(pred_value)):
    pred_value[i].append("-->")
    pred_value[i].append(logic(pred_value[i]))
    print(pred_value[i])

#TODO: написать метод, который создает и заполняет список pred_value автоматически ввсеми возможными комбинациями предикат, потом хорошо бы добавить метод, чтобы печатал красиво, а не со знаками препинания