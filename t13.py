print('13. Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.')

s1 = input('Введите любую строку: ')
s2 = input('Введите символ или их последовательность для подсчета в первой строке: ')
print(f'{s2} встречается в строке - {s1.count(s2)} раза')