print("5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30")

def isfold (a, b):
    if a % b == 0: return True
    else: return False

n = 25 #True
m = 60 #False

ab = isfold(n, 5) and isfold(n, 10)
print(ab)