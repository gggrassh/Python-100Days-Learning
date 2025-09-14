'''
列表的增删
'''
counters = [1,1,1,2,3,5,4,7,6,9,8,10]
# counters.append(11) #末尾增加
# counters.insert(1,12) #插入
# print(counters)

# counters.remove(1) #删除指定元素,若列表中有多个相同元素，只删除一个
# counters.pop() #删除最后一个元素
# counters.pop(1) #删除特定元素
# print(counters)
# # counters.clear() #清空整个列表
# # print(counters)
#
# del counters[5] #删除第六位
# print(counters)

#sort可以实现列表的排序，
counters.sort()
print(counters)
#reverse实现列表的反转
counters.reverse()
print(counters)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swfit'))      # 0
# 从索引位置3开始查找'Java'
# print(items.index('Java', 3))    # ValueError: 'Java' is not in list