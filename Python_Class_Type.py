
#coding:utf-8
#/usr/bin/python3

#type 是用于求一个未知数据类型对象，而 isinstance 是用于判断一个对象是否是已知类型。
#type 不认为子类是父类的一种类型，而isinstance会认为子类是父类的一种类型。
#可以用 isinstance 判断子类对象是否继承于父类，type 不行。
#综合以上几点，type 与 isinstance 虽然都与数据类型相关，但两者其实用法不同，type 主要用于判断未知数据类型，isinstance 主要用于判断 A 类是否继承于 B 类：

# 判断子类对象是否继承于父类
class father(object):
    pass
class son(father):
    pass
if __name__ == '__main__':
    print type(son())==father
    print isinstance(son(),father)
    print type(son())
    print type(son)
#以上实例执行结果为：
#
#False
#True
#<class '__main__.son'>
#<type 'type'>

#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

#以上实例执行结果为：
#
#<__main__.Test instance at 0x100771878>
#__main__.Test
#从执行结果看出，self代表的是类的实例，代表当前对象的地址，而self.class则指向类
#self不是python的关键字，把它换成runoob也是可以正常执行的
