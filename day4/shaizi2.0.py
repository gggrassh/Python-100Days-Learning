import random

counters = [0]*6

for _ in range(6000):
    number = random.randrange(1,7)
    counters[number - 1] += 1
for number in range(1,7):
    print(f'{number}面出现了{counters[number - 1]}次')