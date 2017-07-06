# _*_ coding: utf-8 _*_

#01-原地交换两个数字
x, y = 10, 20
print(x, y)
#(10, 20)

x, y = y, x
print(x, y)
#(20, 10)


#02-链状比较操作符
n = 10
result = 1 < n < 20
print result
#True

result = 1 > n <= 9
print(result)
#False


#03-使用三元操作符来进行条件赋值
def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)

print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))
#0,1,2,3


#04-多行字符串
#将字符串分为多行，并且将整个字符串包含在括号中
multiStr = ("select * from multi_row "
            "where row_id < 5 "
            "order by age")
print(multiStr)
#select * from multi_row where row_id < 5 order by age


#05-存储列表元素到新的变量中
#可以使用列表来初始化多个变量，在解析列表时，变量的数目不应该超过列表中的元素个数
testList = [1, 2, 3]
x, y, z = testList
print(x, y, z)
#(1, 2, 3)


#06-打印引入模块的文件路径
import threading
import socket
print(threading)
print(socket)
#<module 'threading' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.pyc'>
#<module 'socket' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.pyc'>


#07-字典集合推导
testDict = {i:i*i for i in xrange(10)}
testSet = {i*i for i in xrange(10)}
print(testDict)
print(testSet)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#set([0, 1, 4, 81, 64, 9, 16, 49, 25, 36])


#08-检查python中的对象
testCheck = [1, 3, 5, 7]
print(dir(testCheck))
#['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#09-简化if语句
#可以使用下面的方式来验证多个值
#if m in [1, 2, 3]:

#10-运行时检测python 版本
#当正在运行的版本低于支持的版本时，如果不想运行程序，可以使用下面的代码片段终止程序，并读到当前python 版本
import sys
if not hasattr(sys, "hexversion")or sys.hexversion != 50660080:
    print("sorry, you aren't running on python 3.5n")
    print("please upgrade to 3.5.n")
#sys.exit(1)

print("current python version:", sys.version)


#11-组合多个字符串(#注意引号这里有空格符)
testMutli = ['I', 'Like', 'Python', 'automation']
print ' '.join(testMutli)
#I Like Python automation


#12-设定可变参数的默认值
def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list

print bad_append('one')
print bad_append('one')

def bad_append02(new_item,a_list=None):
    if a_list is None:
        a_list=[]
    a_list.append(new_item)
    return a_list

print bad_append02('two')
print bad_append02('two')
#['one']
#['one', 'one']
#['two']
#['two']


#13-四种翻转字符串/列表的方式
testList = [1, 3, 5]
testList.reverse()
print(testList)
#[5, 3, 1]


for element in reversed([1, 3, 5]):
    print(element)
#5
#3
#1

#一行代码翻转字符串
#“test python”[::-1]

#使用切片翻转列表
#[1, 3, 5][::-1]


#14-使用枚举可以在循环中方便地找到当前的索引
testList = [10, 20, 30]
for i, value in enumerate(testList):
    print(i, ':', value)
#(0, ':', 10)
#(1, ':', 20)
#(2, ':', 30)


#15-在python中使用枚举量
class shapes:
    circle, square, triangle, quadrangle = range(4)
print(shapes.circle)
print(shapes.square)
print(shapes.triangle)
print(shapes.quadrangle)
#0
#1
#2
#3


#16-从方法中返回多个值
def x():
    return 1, 2, 3, 4
a, b, c, d = x()
print(a, b, c, d)
#(1, 2, 3, 4)


#17-使用*运算符来unpack函数参数
def test(x, y, z):
    print(x, y, z)
testDict = {'x':1, 'y':2, 'z':3}
testList = [10, 20, 30]
test(*testDict)
test(**testDict)
test(*testList)
#('y', 'x', 'z')
#(1, 2, 3)
#(10, 20, 30)


#18-使用字典来存储选择操作
#我们能构造一个字典来存储表达式
stdCalc = {
    'sum':lambda x, y: x + y,
    'subtract':lambda x, y: x- y
}

print(stdCalc['sum'](9,3))
print(stdCalc['subtract'](9,3))
#12
#6


#19-一行代码计算任何数的阶乘
result = (lambda k: reduce(int.__mul__, range(1, k+1), 1))(6)
print(result)
#720


#20-找到列表中出现最频繁的数
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))
#4


#21-重置递归限制
#python限制递归次数到1000，可以修改这个值
x = 1001
print(sys.getrecursionlimit())

sys.setrecursionlimit(x)
print(sys.setrecursionlimit())
#1000
#1001


#22-检查一个对象的内存使用
#在python2.7中，一个32比特的整数占用24字节，在Python3.5中占用28字节
x = 1
print(sys.getsizeof(x))
#24


#23-从两个相关的序列构建一个字典
t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict (zip(t1,t2)))
#{1: 10, 2: 20, 3: 30}


#24-一行代码搜索字符串的多个前后缀
print("http://www.google.com".startswith(("http://", "https://")))
print("http://www.google.co.uk".endswith((".com", ".co.uk")))
#True
#True


#25-不使用循环构造一个列表
import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))
#[-1, -2, 30, 40, 25, 35]


#26-在 Python 中实现一个真正的 switch-case 语句
def xswitch(x):
    return xswitch._system_dict.get(x, None)

xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(xswitch('default'))
print(xswitch('devices'))
#None
#2


