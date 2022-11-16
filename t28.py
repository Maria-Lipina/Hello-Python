print("30. Вычислить число pi c заданной точностью d. Пример: при d = 0.001, pi = 3.141. 10^1>=d>=10^-10")

def leibniz_pi(d):
    d = len(str(d))
    k = 1
    pi = 0
    for i in range(1_000_000):
        if i % 2 == 0:
            pi += 4/k
        else: pi -= 4/k
        k += 2
    pi = str(pi)
    return (pi[:d])

print(leibniz_pi(0.001))