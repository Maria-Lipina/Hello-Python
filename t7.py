from pickle import TRUE


print("7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат")

def logic(x, y, z):
    return not (x or y or z) == (not x and not y and not z)


def truth_table():  # TT
    result = []
    for x in [True, False]:
        for y in [True, False]:
            for z in [True, False]:
                result.append([x, y, z, logic(x, y, z)])
    return result


def print_TT():
    data = truth_table()
    line = ""
    print("X\tY\tZ\tExpression\t")
    for i in range(len(data)):
        for j in data[i]:
            line += f"{j}\t"
        print(line)
        line = ""


print_TT()
