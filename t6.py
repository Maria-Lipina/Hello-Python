print("6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.")

import random

def define_day(no):
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье',]
    if d in range(0,7):
        if d == 6 or d == 5:
            return f'{week[d]} - выходной'
        else: return f'{week[d]} - будний'
    else: return "not a week day"



d = random.randint(0, 6)
print(define_day(d))