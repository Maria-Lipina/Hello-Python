# Найти максимальное из пяти чисел
#TODO: убрать print a из самого метода, но при этом он остается, как дополнительная информация для пользователя. Если разберусь с globals в exec, то возможно, получится перенести import random в глобальный контекст

def do():
    import random
    a = [random.randint(0, 1000) for i in range(5)]
    print(a)
    return max(a)
