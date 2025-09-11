import random
answer = random.randint(1, 100)
counter = 0
while True:
    counter = counter + 1
    x = int(input('请输入数字：'))
    if x < answer:
        print('小了')
    elif x > answer:
        print('大了')
    else:
        print('猜对了！')
        break
print(f'你一共猜了{counter}次')