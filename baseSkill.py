# _*_ coding: utf-8 _*_

#01-原地交换两个数字
x, y = 10, 20
print(x, y)

x, y = y, x
print(x, y)


#01-链状比较操作符
n = 10
result = 1 < n < 20
print result

result = 1 > n <= 9
print(result)


#03-使用三元操作符来进行条件赋值
def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)

print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))


#04-多行字符串
#将字符串分为多行，并且将整个字符串包含在括号中
multiStr = ("select * from multi_row "
            "where row_id < 5 "
            "order by age")
print(multiStr)


#05-存储列表元素到新的变量中
#可以使用列表来初始化多个变量，在解析列表时，变量的数目不应该超过列表中的元素个数
testList = [1, 2, 3]
x, y, z = testList
print(x, y, z)


#06-打印引入模块的文件路径
import threading
import socket
print(threading)
print(socket)

#07-字典集合推导
testDict = {i:i*i for i in xrange(10)}
testSet = {i*i for i in xrange(10)}
print(testDict)
print(testSet)


#08-检查python中的对象
testCheck = [1, 3, 5, 7]
print(dir(testCheck))


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


#11-组合多个字符串
testMutli = ['I', 'Like', 'Python', 'automation']
print ' '.join(testMutli)


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



