import math
print("15. Написать программу получающую набор произведений чисел от 1 до N. \n Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]")

n = 7
result = [math.factorial(i) for i in range(1, n+1)]
print (result) 
