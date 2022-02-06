print("20. Определить, присутствует ли в заданном списке строк, некоторое число ")

import randomizer as rdm

li_str = ','.join(rdm.fill_str_list(5, 10))
print(li_str)
print ('10' in li_str)

#Как с помощью weight, cum_weight задать методу преференцию на выбор чисел из общей популяции? The number of weights does not match the population - как это работает?