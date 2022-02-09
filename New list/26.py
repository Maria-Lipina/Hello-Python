print("26. Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. ")

def fib(n):
    if n in [1, 2]: return 1
    elif n < 1: return 0
    else: return fib(n-1) + fib(n-2)

def negafib(n):
    return ((-1)**(n+1))*fib(n)

n = 10
res = [None for i in range(1 + n*2)]
res[n] = 0
j = 1
for i in range(n+1, len(res)):  
    res[i] = fib(j)
    res[-i-1] = negafib(j)
    j = j + 1
print(res)

exit()
"""

n	...	−10	   −9	  −8	−7	 −6	   −5	−4	  −3	−2	 −1	  0	   1	  2	   3 	4	 5	  6	   7	 8	  9	    10	…
  ...	−55	   34	  −21	13	 −8	   5	−3	  2 	−1	  1	  0	   1	  1	   2	3	 5	  8	   13	 21	  34	55	…
[None,  -55    34     -21   13   -8,   5    -3    2     -1    1   1    1      2    3    5    8    13   21    34   55]
 0      1      2      3     4     5    6    7     8     9    10  11   12     13   14   15   16    17   18    19   20
-21    -20    -19    -18   -17   -16 -15   -14   -13   -12  -11  -10   -9     -8   -7   -6   -5    -4   -3    -2   -1                                   -7     -6     -5      -4 -3-2   -1
                                                              n   n+1
                                                                  res i начало цикла fib1 = 1
                                                        negafib = 1

"""

# def fiblist(n):
#     res = [None] * (1 + n*2)
#     res[n] = 0
#     for i in range(n+1, len(res)):
#         res[i] = fib(i)
#         res[-i] = negafib(i)




# list_f = []
# li_test = []
# for e in range(1, 11):
#     list_f.append((fib(e)))
#     li_test.append(negafib(e))
# print (list_f)
# print (li_test)

