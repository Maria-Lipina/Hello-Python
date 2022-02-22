print("27. Строка содержит набор чисел. Показать большее и меньшее число Символ-разделитель - пробел")

numstr = '12 443 76 656 53 86 932 342 123 56 777'
nums = [int(i) for i in numstr.split()]
print(f'min = {min(nums)}, max = {max(nums)}')