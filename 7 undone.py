print("7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат")
"                                          2   1   1       3  6 4  6 5"
#TODO: Короче написать метод, который печатает таблицу со всеми значенями предикат, потом добавить сюда ещё и выражение

def logic (x, y, z):
    xyz_or = x or y or z
    print(xyz_or)
    notxyz = not xyz_or
    print(notxyz)
    nots_xyz_and = not x and not y and not z
    print(nots_xyz_and)
    expression = notxyz == nots_xyz_and
    return expression

x, y, z = True, True, True, 
# print(logic(x, y, z))
x, y, z = False, True, True,
# print(logic(x, y, z))
x, y, z = True, False, True,
print(logic(x, y, z))