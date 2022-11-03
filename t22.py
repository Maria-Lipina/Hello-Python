import random

print("22. Найти сумму чисел списка стоящих на нечетной позиции")


def sum_odd_positions(input: list):
    sum_odds = 0
    for i in range(1, len(input), 2):
        sum_odds = sum_odds + input[i]
    return sum_odds


input = [random.randrange(-10, 11) for i in range(5)]
print(input)
print(sum_odd_positions(input))