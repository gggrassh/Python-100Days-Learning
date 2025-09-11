'''for-in循环'''
# import time
# for i in range(5):
#     print(i)
#     time.sleep(1)

# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。

'''不使用循环变量i'''
# 大家可能已经注意到了，上面代码的输出操作和休眠操作都没有用到循环变量i，
# 对于不需要用到循环变量的for-in循环结构，按照 Python 的编程惯例，我们通常把循环变量命名为_
# import time
# for _ in range(5):
#     print('lemon')
#     time.sleep(1)

'''1到100求和'''
# x = 0
# for i in range(1,101):
#     x = x+i
# print(x)

'''1到100偶数求和'''
# x = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         x = x + i
# print(x)

'''while循环'''
# x = 0
# i = 1
# while i < 101:
#     x = x + i
#     i = i + 1
# print(x)

'''break and continue'''
# import time
# x = 0
# i = 2
# while True:
#     x = x + i
#     i = i + 2
#     time.sleep(1)
#     print(x)
#     # if i >100:
#     #     break
# # print(x)

# x = 0
# i = 1
# while i < 101:
#     x = x + i
#     i = i + 1
#     if i % 2 != 0:
#         continue
# print(x)

'''九九乘法表'''
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}x{j}={i * j}', end='\t')
#     print()