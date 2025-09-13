"""
列表
"""
# 在 Python 中，列表是由一系元素按特定顺序构成的数据序列，这就意味着如果我们定义一个列表类型的变量，可以用它来保存多个数据。在 Python 中，可以使用[]字面量语法来定义列表，列表中的多个元素用逗号进行分隔，代码如下所示。
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
items4 = list(range(1, 10))
items5 = list('hello')
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']

'''
列表的运算
'''
items6 = items1 + items2
items5 += items4
print(items6)
print(items5)

#列表的重复运算
print(items3*2)

#用in或not in运算符判断一个元素在不在列表中
print('h' in items5)
print('h' in items4)

'''
由于列表中有多个元素，而且元素是按照特定顺序放在列表中的，所以当我们想操作列表中的某个元素时，
可以使用[]运算符，通过在[]中指定元素的位置来访问该元素，这种运算称为索引运算。需要说明的是，
[]的元素位置可以是0到N - 1的整数，也可以是-1到-N的整数，分别称为正向索引和反向索引，
其中N代表列表元素的个数。对于正向索引，[0]可以访问列表中的第一个元素，[N - 1]可以访问最后一个元素；
对于反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素，代码如下所示。
'''
items7 = [1,2,3,4,5,6,7,8,9,10]
print(items7[0])
print(items7[2])
print(items7[-1])
# items7[2]=11
# print(items7)
# print(items7[2])

# 如果希望一次性访问列表中的多个元素，我们可以使用切片运算。
# 切片运算是形如[start:end:stride]的运算符，其中start代表访问列表元素的起始位置，
# end代表访问列表元素的终止位置（终止位置的元素无法访问），而stride则代表了跨度，
# 简单的说就是位置的增量，比如我们访问的第一个元素在start位置，
# 那么第二个元素就在start + stride位置，当然start + stride要小于end。
# 我们给上面的代码增加下面的语句，来使用切片运算符访问列表元素。
print(items7[1:5:1])
print(items7[0:4:2])
print(items7[-1:-5:-1])
print(items7[-5:-1:1])

# 如果start值等于0，那么在使用切片运算符时可以将其省略；如果end值等于N，
# N代表列表元素的个数，那么在使用切片运算符时可以将其省略；如果stride值等于1，
# 那么在使用切片运算符时也可以将其省略。所以，下面的代码跟上面的代码作用完全相同。
print(items7[::2])
print(items7[::])
print(items7[1:3])
#还可以通过切片操作修改列表中的元素
items7[1:3]=['a','b']
print(items7)