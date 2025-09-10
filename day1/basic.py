'''
the first project
'''
#test1
print('test1')

'''
整形
'''
print(0b100) #二进制整数
print(0o100) #八进制整数
print(100) #十进制整数
print(0x100) #十六进制整数

'''
浮点型
'''
print(123.456)
print(1.23456e2)

'''
字符串
'''
print('test')

'''
变量
'''
a = 45        # 定义变量a，赋值45
b = 12.1       # 定义变量b，赋值12.1
e = a + b
print(a, b)
print(e)
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75
#使用type检查变量类型
c='l'
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
可以通过 Python 内置的函数来改变变量的类型，下面是一些常用的和变量类型相关的函数。

int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
'''
print(int(e))
print(float(a))
print(str(a))
print(ord(c))

f=10
g=3

print((j:=20))
print(j)
print((h:=10))
print(h)