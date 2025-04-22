# 基本装饰器
# def decorator_eg(func):
#     def wrapper():
#         print("在执行函数之前，进行的操作")
#         func()  # 回调
#         print("装饰器可以继续添加功能")
#     return wrapper  # 返回闭包函数对象
#
#
# @decorator_eg   # 语法糖，相当于 func_eg = decorator_eg(func_eg)
# def func_eg():
#     print("这是一个函数，执行某个功能")
#
# func_eg()

# 带参装饰器
# 1. 被装饰函数有参数
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         # 调用被装饰的函数，并将返回值保存到变量中
#         result = func(*args, **kwargs)
#         print("After function call")
#         return result    # 返回被装饰函数的返回值
#     return wrapper    # 返回闭包函数
#
# @my_decorator
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# """
# 1. result的return是闭包函数的返回值，用于存储func()的运行结果
#     （1）保证被装饰后的函数在调用时，能和原始函数一样返回正确的结果
#     （2）支持链式调用和后续处理
# 2. 作为装饰器，my_decorator()的返回值是wrapper这个闭包函数
# """

# 2. 装饰器自身有参数
# def repeat(n):    #装饰器自身的参数
#     def decorator(func):    #装饰器本身，接收被装饰函数作为参数
#         def wrapper(*args, **kwargs):    #闭包函数，接收被装饰函数的参数
#             # 对被装饰函数进行处理
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result    # 返回被装饰函数的返回值
#         return wrapper    # 返回闭包函数
#     return decorator    # 返回装饰器本身
#
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}")
#
# greet("DVA")

# 3. 装饰器链
# def decorator1(func):
#     print("应用了装饰器1")
#     def wrapper():
#         print("装饰器1的前置逻辑")
#         func()
#         print("装饰器1的后置逻辑")
#     return wrapper
# def decorator2(func):
#     print("应用了装饰器2")
#     def wrapper():
#         print("装饰器2的前置逻辑")
#         func()
#         print("装饰器2的后置逻辑")
#     return wrapper
#
# @decorator1
# @decorator2
# def my_function():
#     print("原始函数的逻辑")
#
# my_function()

# class MyClass:
#     @classmethod
#     def class_method(cls):
#         print(f"这是一个类方法，cls的值为: {cls}")
#
# MyClass.class_method()
# # 输出：这是一个类方法，cls的值为: <class '__main__.MyClass'>

#类方法作为工厂函数
# 类方法创建单例
# class Single:
#     instance = None
#     @classmethod
#     def get_instance(cls):
#         if cls.instance is None:
#             cls.instance = cls() #等同于Single()，创建一个对象
#             return cls.instance
#         else:
#             return cls.instance
# s1 = Single.get_instance()
# s2 = Single.get_instance()
# print(id(s1))   # 46752
# print(id(s2))   # 46752

# 类方法批量创建对象
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def create_student(cls,count=20):
#         stu_list = []
#         for i in range(count):
#             stu_list.append(Student(f"Student{i+1}",i+1))
#         return stu_list
# # 普通方式创建对象
# s1 = Student("张三",18)
# # 批量创建对象
# result = Student.create_student(10)
# print(result)

# class Circle:
#     # 类属性
#     pi = 3.14
#
#     @staticmethod
#     def calculate_area(radius):
#         # 以下代码会报错，因为静态方法没有 cls 参数，无法直接访问类属性
#         # return cls.pi * radius * radius
#         # 通过类名间接访问类属性
#         return Circle.pi * radius * radius
#
#
# # 调用静态方法
# c1 = Circle()
# area1 = c1.calculate_area(10)   # 静态方法可以通过类名或对象名调用
# area2 = Circle.calculate_area(5)
# print(area1,area2)  # 输出：314.0 78.5

# # __new__ 方法中实现单例模式
# class MyClass:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#         else:
#             return cls._instance
#
# s1 = MyClass()
# s2 = MyClass()
# print(s1 is s2) # True
"""
魔术方法===========================================================================
"""
# # 魔术方法
#
# class Cat:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#         self.cat_list = ["米努特","布偶","金渐层"]
#     def __call__(self, *args, **kwargs):
#         print("我是一只猫，我叫" + self.name)
#         print("像调用函数一样调用了我", *args, **kwargs)
#
# c1 = Cat("酱酱",3)
# print(callable(c1))
# c1()

# class Cat:
#     def __init__(self, name,age):
#         self.__name = name
#         self._age = age
#     def set_name(self,name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#
# c1 = Cat("酱酱",3)
# print(c1._age)   # 3
# c1._age = 5
# print(c1._age)   # 5
# #单下划线开头的属性和方法，是约定俗成的，不是强制的
# # age是公开属性，可直接访问和修改
# #双下划线开头的属性和方法，是私有属性和方法，不能直接访问和修改
# # 私有属性，只能通过方法访问和修改
# # print(c1.name)  #报错
# c1.name = "酿酿"  # 不会报错，但是不会修改私有属性
# print(c1.get_name())    # 酱酱
# c1.set_name("酿酿")
# print(c1.get_name())    # 酿酿



class Mammal:
    def shoot(self):
        print("吼叫")
class Cat(Mammal):
    def shoot(self):
        print("小猫呼噜" )
class Dog(Mammal):
    def shoot(self):
        print("小狗汪汪")
def func(Mammal):
    Mammal.shoot()

Jiang = Cat()
Chuang = Dog()
func(Jiang)
func(Chuang)













