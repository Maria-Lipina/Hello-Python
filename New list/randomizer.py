import random
import datetime
import string

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


def fill_str_list(el_len, li_len): #20.py, если что-то изменится. Все-таки искусственно увеличивать вероятность цифр через многократную конкатенацию - не очень красиво
    result = []
    for i in range(li_len):
        result.append(''.join(random.choices(string.ascii_letters + string.digits + string.digits + string.digits + string.digits, k = el_len))) #сплагиачено
    return result


""" TODO: чем str отличается от string? Кроме built-in https://docs.python.org/3.10/library/stdtypes.html#textseq 
https://docs.python.org/3.10/library/string.html?highlight=string#module-string 
"""