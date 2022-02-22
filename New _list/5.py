print("5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30")

import random

def isfold (a, b):
    if a % b == 0: return True
    else: return False

n = random.randrange(0, 101, 5)

ab = isfold(n, 5) and isfold(n, 10) \
    or isfold(n, 15) and not isfold(n, 30)
print(f'{n} -- {ab}')

