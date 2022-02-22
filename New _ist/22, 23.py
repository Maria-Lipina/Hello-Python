import randomizer as rdm

source = rdm.fill_list(19, 0, 10)
print(source)


print("22. Найти сумму чисел списка стоящих на нечетной позиции")

sum_odds = 0
for i in range(1, len(source), 2): sum_odds = sum_odds + source[i]
print(sum_odds)


print("23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.") 
"""Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]"""

res = [source[i] * source[-1-i] for i in range(round(len(source) / 2))]
print(res)