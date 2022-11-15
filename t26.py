print("26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. ")

def fib(n):
    if n in [1, 2]: return 1
    elif n < 1: return 0
    else: return fib(n-1) + fib(n-2)

def fiblist(n):
    res = [0 for i in range(1 + n*2)]
    j = 0
    for i in range(n+1, len(res)):
        j = j + 1
        if j % 2:
            res[i] = res[-i-1] = fib(j)
        else: 
            res[i] = fib(j)
            res[-i-1] = -res[i]
    return res

full_fibonacchi = fiblist(35)
print(full_fibonacchi)
