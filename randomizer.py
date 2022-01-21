import random

print(random.randint(0, 20))
print(random.randrange(100))
print(random.randrange(0, 15, 3)) #This fixes the problem with randint() which includes the endpoint; in Python this is usually not what you want.
