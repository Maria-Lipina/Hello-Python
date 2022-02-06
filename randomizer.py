import random
import datetime

def fill_list(length, min, max): #2.py, если что-то изменится
    result = []
    for i in range(length):
        result.append(random.randint(min, max))
    return result

def seed():
    moment = str(datetime.datetime.now())
    for i in moment:
        if i == '-' or i == ' ' or i == ':' or i == '.':
            moment = moment.replace(i, '')

    seed = []
    for i in range(1, len(moment)+1):
        if not i % 2:
            seed.append(int(moment[i-2:i]))
    return seed
