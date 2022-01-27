print("7. Показать числа от -N до N")

import random

n = random.randrange(100)
print(list(range(-n, n+1)))