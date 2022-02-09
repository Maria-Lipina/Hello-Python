print("26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. ")

def fib(n):
    if n in [1, 2]: return 1
    elif n < 1: return 0
    else: return fib(n-1) + fib(n-2)

def negafib(n):
    return ((-1)**(n+1))*fib(n)

def fiblist(n):
    res = [None for i in range(1 + n*2)]
    res[n] = 0
    j = 1
    for i in range(n+1, len(res)):
        res[i] = fib(j)
        res[-i-1] = negafib(j)
        j = j + 1
    return res

full_fibonacchi = fiblist(10)
print(full_fibonacchi)