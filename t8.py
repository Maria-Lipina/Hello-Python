from random import randint

print("8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У ")


def random_dot(limit):
    return [randint(-limit, limit), randint(-limit, limit)]


def quarter(dot):
    if dot[0] == 0:
        return 'ось X'
    if dot[1] == 0:
        return 'ось Y'
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    elif dot[1] > 0:
        return 2
    else:
        return 3

# импортируется и вызывается в t10
# print(
#     quarter(
#         random_dot(30)
#     ))
