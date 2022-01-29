matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
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

for i in range(len(matrix)):
    matrix[i].append("-->")
    matrix[i].append(100)
    print(matrix[i])
