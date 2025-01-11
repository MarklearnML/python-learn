str1 = "Hello"

# 1. 字符串的切片操作
print(str1[0:3])
print(str1[0:])
print(str1[:3])
print("====================")
# 2. 字符串的拼接
print(str1 + " World")
print(str1 * 3)
print("====================")
# 3. 字符串的不可变性
str2 = str1
str1 += " World"
print(str1)
print(str2)
print("====================")
# 4. 字符串的内置函数
str1 = "Hello World"
print(len(str1))  # 获取字符串的长度
print(str1.find("World"))  # 查找子字符串"World"在str1中的位置，如果不存在返回-1
print(str1.count("l"))  # 计算字符"l"在str1中出现的次数
print(str1.replace("World", "Python"))  # 将str1中的"World"替换为"Python"
print(str1.split(" "))  # 以空格为分隔符，将str1分割成一个列表
print(str1.upper())  # 将str1中的所有字母转换为大写
print(str1.lower())  # 将str1中的所有字母转换为小写
print(str1.capitalize())  # 将str1的第一个字符转换为大写，其余字符转换为小写


