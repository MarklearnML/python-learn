# 魔法方法总结
# 1 初始化和表示
# __init__: 初始化对象
# __new__: 创建对象
# __str__: 打印对象
# __repr__: 打印对象
# __del__: 删除对象
# 单例模式
class Person:
    _instance = None
    def __new__(cls, *args, **kwargs):
        print("__new__")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    
    def __init__(self, private):
        self.private = private
        print("__init__")
        print(self.private)

    
person = Person("private")
person1 = Person("private")
print(person)
print(person1)

# 2. 类容器
# __len__: 返回容器的长度
# __getitem__: 获取容器中的元素
# __setitem__: 设置容器中的元素
# __delitem__: 删除容器中的元素
# __iter__: 返回容器的迭代器
# __next__: 返回容器的下一个元素
# __contains__: 判断容器中是否包含某个元素
# __reversed__: 返回容器的反向迭代器
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print("gititem" + str(index))
        return self.data[int(index/2)]
    
    def __len__(self):
        return 2
myList = MyList([1, 2, 3, 4, 5, 6])
for i in myList:
    print(i)
print(len(myList))

# 3. __call__  把类当成函数调用

class CallTest:
    "测试__doc__"
    name1 = "calltest"
    def __call__(self, *args, **kwargs):
        print("call" + args[0])
    def __init__(self):
        self.name = "calltest"
        self.age = 18
        pass
    
calltest = CallTest()
calltest("hello")
print(calltest.__dict__)
print(dir(calltest))
print(calltest.__doc__)
#__dir__的作用是什么？
#__dir__的作用是返回对象的所有属性和方法，包括类的属性和方法，以及实例的属性和方法。
# 如何使用呢？
# 使用dir(对象)，返回的是一个列表，列表中是对象的所有属性和方法。