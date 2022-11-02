import string
from random import choices

print("20. Определить, присутствует ли в заданном списке строк, некоторое число ")

def num_in_string_list (num, li_str):
    num = str(num)
    res = False
    for s in li_str:
        if num in s: res = True
    return res    

input = [''.join(choices(string.ascii_letters + string.digits*6, k=7))
         for i in range(10)]

print(input)
print(num_in_string_list(1, input))
