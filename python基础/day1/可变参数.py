list = [1, 2, 3]

# 1. 列表的切片操作
print(list[0:3])
print(list[0:])
print(list[:3])
print(list[1])
print("====================")


# 2. 列表的拼接
print(list + [4, 5, 6])
print(list * 3)
print("====================")

# 3. 列表的可变性
list2 = list
list.append(4)
print(list)
print(list2)
print("====================")

# 4. 列表的内置函数
list = [1, 2, 3]
print(len(list))  # 获取列表的长度
print(max(list))  # 获取列表中的最大值
print(min(list))  # 获取列表中的最小值
print(list.index(2))  # 获取元素2在列表中的位置
print(list.count(2))  # 统计元素2在列表中出现的次数
list.append(4)  # 在列表末尾添加元素4
print(list)
list.insert(0, 0)  # 在列表的指定位置插入元素0
print(list)
list.remove(0)  # 删除列表中的元素0
print(list)
list.pop()  # 删除列表中的最后一个元素
print(list)
list.reverse()  # 反转列表
print(list)
list.sort()  # 对列表进行排序
print(list)
 
 # 5. 列表的遍历
for i in list:
    print(i)
    
    
dict = {"name": "Tom", "age": 18, "gender": "male"}

# 1. 字典的操作
print(dict["name"])
print(dict.get("name"))
dict["name"] = "Jerry"
print(dict)
dict.pop("name")
print(dict)
dict.clear()
print(dict)

# 2. 字典的可变性
dict = {"name": "Tom", "age": 18, "gender": "male"}
dict2 = dict
dict["age"] = 20
print(dict)
print(dict2)

# 3. 字典的遍历
for key in dict:
    print(key, dict[key])

for key, value in dict.items():
    print(key, value)
    
print(type(dict)) 
print(type(list))


# 元组 （不可变）
tuple = (1, 2, 3)
print(type(tuple))

tuple2 = tuple
tuple = (4, 5, 6)
print(tuple)
print(tuple2)
print(tuple[1])