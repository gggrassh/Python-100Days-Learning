weight=float(input('weight（KG）='))
height=float(input('height（M）='))
BMI=weight/(height*height)
print(BMI)
if 18.5<=BMI<=25:
    print('你很健康!')
else:
    print('你的身材不太标准')