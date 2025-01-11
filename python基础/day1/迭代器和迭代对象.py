import sys

# 设置标准输出编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')
# 迭代对象
# 可迭代对象：可以直接作用于for循环的对象统称为可迭代对象（Iterable）
# 可迭代对象包括：
# 1. 集合（set）
# 2. 列表（list）
# 3. 元组（tuple）
# 4. 字典（dict）
# 5. 字符串（str）
from collections.abc import Iterable

print(isinstance(set([1,2,3]), Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({"name": "Tom", "age": 18, "gender": "male"}, Iterable))
print(isinstance("Hello", Iterable))


# 迭代对象变成迭代器的案例

# 1. 使用字符串创建迭代器
print("1. 字符串迭代器:")
string = "Python"
string_iterator = iter(string)
print(next(string_iterator))  # 输出: P
print(next(string_iterator))  # 输出: y
print(next(string_iterator))  # 输出: t

# 2. 使用列表创建迭代器
print("\n2. 列表迭代器:")
my_list = [1, 2, 3, 4, 5]
list_iterator = iter(my_list)
print(next(list_iterator))  # 输出: 1
print(next(list_iterator))  # 输出: 2
print(next(list_iterator))  # 输出: 3

# 3. 使用元组创建迭代器
print("\n3. 元组迭代器:")
my_tuple = ('a', 'b', 'c')
tuple_iterator = iter(my_tuple)
print(next(tuple_iterator))  # 输出: a
print(next(tuple_iterator))  # 输出: b
print(next(tuple_iterator))  # 输出: c

# 4. 使用for循环遍历迭代器
print("\n4. 使用for循环遍历迭代器:")
my_list = [10, 20, 30, 40, 50]
my_iterator = iter(my_list)
for item in my_iterator:
    print(item, end=' ')  # 输出: 10 20 30 40 50

# 5. 演示迭代器耗尽
print("\n\n5. 迭代器耗尽:")
my_iterator = iter([1, 2, 3])
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
print(next(my_iterator))  # 输出: 3
try:
    print(next(my_iterator))  # 将引发 StopIteration 异常
except StopIteration:
    print("迭代器已经耗尽")
