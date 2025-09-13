import random
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randrange(1,7)
    if face == 1:
        f1 = f1 + 1
    elif face == 2:
        f2 = f2 + 1
    elif face == 3:
        f3 = f3 +1
    elif face == 4:
        f4 = f4 + 1
    elif face == 5:
        f5 = f5 + 1
    else:
        f6 = f6 + 1
print(f'1：{f1}次，2：{f2}次，3：{f3}次，4：{f4}次，5：{f5}次，6：{f6}次')