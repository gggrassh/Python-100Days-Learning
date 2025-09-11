print('请输入你的分数')
x=int(input())
if x > 90:
    grade = 'A'
elif x > 80:
    grade = 'B'
elif x > 70:
    grade = 'C'
elif x > 60:
    grade = 'D'
else:
    grade = 'F'
print(f'{grade}')