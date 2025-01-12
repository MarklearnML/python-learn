# 生成器的解释
# 生成器就是一个特殊的迭代器，可以通过next()函数获得下一个值，但是它不占用额外的内存空间。    
# 生成器的语法如下：

# 1. 使用yield关键字定义生成器函数
def count(n):
    while n > 0:
        yield n
        n -= 1
    
fun = count(5)
print(next(fun))
print(next(fun))
print(next(fun))

for i in fun:
    print(i)
    
# 2. 带参数的生成器函数
def count1(n):
    while n > 0:
        y = yield n
        n -= 1
        if y is not None:
            n += y
            
fun1 = count1(5)
print(fun1.send(None))
print(fun1.send(5))
print(fun1.send(None))
print(fun1.send(None))
