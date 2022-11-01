import random

print("18. Реализовать алгоритм перемешивания списка.")

def shuffle(li):
    for i in range(len(li)):
        ind = random.randrange(len(li)-i)
        temp = li[len(li)-1-i]
        li[len(li)-1-i] = li[ind]
        li[ind] = temp

li_in = list(range(1,20))
print(li_in)
shuffle(li_in)
print(li_in)

