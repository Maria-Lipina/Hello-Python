# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
"""
# transposed = [[row[i] for row in matrix] for i in range(4)]
# print(transposed)
#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#https://docs.python.org/3.10/faq/programming.html?highlight=dimensio#how-do-i-create-a-multidimensional-list
альтернатива - numPy, matrix datatypa - это явно слишком сложно и не стоит самой задачи. Но помни, что это быстрее, чем якобы multidimentional lists здесь

# transposed_1 = list(zip(*matrix))
"""
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j])
#     print('\n')

# for i in range(len(matrix)):
#     print(matrix[i])

# for i in range(len(matrix)):
#     matrix[i].append("-->")
#     matrix[i].append(100)
#     print(matrix[i])


def foo(d, e, f):
    print(d, e, f)

a, b, c = 1, 2, 3
foo(a, b, c)                  # Выводит 1, 2, 3
foo(b, a, c)                  # Выводит 2, 1, 3
foo(c, b, a)                  # Выводит 3, 2, 1


def foo(arg1=0, arg2=0, arg3=0):
    print(arg1, arg2, arg3)

a, b, c = 1, 2, 3
foo(a,b,c)                          # Выводит 1 2 3
foo(arg1=a, arg2=b, arg3=c)         # Выводит 1 2 3
foo(arg3=c, arg2=b, arg1=a)         # Выводит 1 2 3
foo(arg2=b, arg1=a, arg3=c)         # Выводит 1 2 3