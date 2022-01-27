import random

def fill_list(length, min, max): #2.py, если что-то изменится
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result
