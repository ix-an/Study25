# 位置传参
# def func1(a,b,c):
#     print(a,b,c)
#     return
# func1(1, 2, 3)

#关键字传参
# def func2(name,age,score):
#     print(name,age,score)
#     return
# func2(age=18,score=100,name="张三")  #关键字传参，位置可以改变
# #func2(18,100,name = "张三")  #这样不行，前面的位置参数必须按顺序传参
# func2("李四",score = 99,age = 20) #位置参数之后的关键字参数可以不按顺序

# #默认值参数
# def func3(name,age=18,score=88):
#     print(name,age,score)
#     return
# func3("张三")    # 不传参则使用默认值
# func3("李四",score = 100,age = 20)    # 后面可以关键字传参，规则相同

#可变位置参数
# def func4(a,b,c,*x):
#     print(a,b,c)
#     print(x,type(x))
# func4(1,2,3)
# func4(1,2,3,4,5)

# #可变关键字参数
# def func5(a,b,**kwargs):
#     print(a,b)
#     print(kwargs,type(kwargs))
# func5(1,3,c=4,d=5,e=6)
# print("-------------------")
# #可以和位置参数一起使用
# def func6(a,b,*arg1,**arg2):
#     print(a,b)
#     print(arg1)
#     print(arg2)
# func6(1,2,55,60,c=100,d=200)
# #以位置参数传入，则是可变位置参数，以关键字参数传入，则是可变关键字参数

# # 多参数解包
# def func7(a,b,c):
#     print(a,b,c)
#     return
# # 解包序列，得到位置参数
# args_list = [1,2,3]
# args_tuple = (1,2,3)
# #func7(args_list)    #报错，相当于把list作为一个参数传入
# # func7(agrs_list[0],args_list[1],args_list[2])   #麻烦的写法
# func7(*args_list)   #解包序列，得到位置参数
# func7(*args_tuple),func7(*range(3))    #序列指可以按顺序取下标的对象
#
# #解包字典，得到关键字参数
# args_dict = {'a':1,'b':2,'c':3}
# func7(**args_dict)
# #需要注意，数量以及名称要一致

# # * 参数
# def func8(name,student_id,*,score,**info):
#     print(f"学号为：{student_id}的{name}你好")
#     print(f"你的分数是：{score}")
#     print(f"其余信息：{info}")
#     return
# func8("张三",1001,score = 100,improve = "10分")
#
# """
# def func(a,*,**kwargs):    #会报错，*后面必须保证有关键字参数
# def func(a,*,*args):    #会报错，*形参只能出现一次，且*参数后面不可能有位置参数
# """

# ==================================================================================

# # 不可变类型实参
# def modify_immutable(n):
#     n += 100
#     print(n,id(n))
# num = 10
# print(num,id(num))      #10 650320
# modify_immutable(num)   #110 84200
# print(num,id(num))      #10 650320
#
# # 可变类型实参
# def modify_mutable(lst):
#     lst.append(100)
#     print(lst,id(lst))
# list1 = [1,2,3]
# print(list1,id(list1))  # [1, 2, 3] 754304
# modify_mutable(list1)   # [1, 2, 3, 100] 754304
# print(list1,id(list1))  # [1, 2, 3, 100] 754304

# # 避免意外修改可变类型实参
# def process_list(lst):
#     lst = lst.copy()
#     lst.append(100)
#     print(lst,id(lst))
# list1 = [1,2,3]
# print(list1,id(list1))  # [1, 2, 3] 553408
# process_list(list1)   # [1, 2, 3, 100] 720384
# print(list1,id(list1))  # [1, 2, 3] 553408

#===================================================================================

# # 匿名函数
# hello = lambda : print("hello world")  #参数列表可以为空
# add = lambda x,y : x + y
# hello()
# print(add(1,2))
#
# # e.g. 使用匿名函数，对列表中的元组按第二个元素进行排序
# list1 = [('a',3),('b',2),('c',1)]
# list_temp_sort = lambda lst: sorted(lst, key = lambda x: x[1])
# print(list_temp_sort(list1))
# # 输出：[('c', 1), ('b', 2), ('a', 3)]

#常见内置函数

# # all()
# list1 = [1,-1,2,0]
# list2 = [1,-2,0.5]
# print(all(list1))    #False
# print(all(list2))    #True
# print(any(list1))    #True
# print(any(list2))    #True

# # sum()
# list1 = [1,2,3,4,5]
# print(sum(list1))    #15

# # 给出一个列表，按照元素离20的距离远近生序排列
# list1 = [-3,19,20,27,15]
# list1_sort = sorted(list1,key = lambda i : (i - 20) ** 2)
# print(list1_sort)

# # reversed()
# tuple1 = (5,4,3,2,1)
# print(reversed(tuple1))
# # <reversed object at 0x000002E21BA1D3D0>
# # 返回的是反向迭代器
# print(tuple(reversed(tuple1)))   #(1, 2, 3, 4, 5)

# # callable()
# test_func = lambda : print("hello world")
# fake_func = 1
# print(callable(test_func))    #True
# print(callable(fake_func))    #False

# # zip()
# name_list = ["张三","李四","王五"]
# age_list = [18,20,22]
# re = zip(name_list,age_list)
# print(re)   # <zip object at 0x0000025E1BA1D3D0>
# print(list(re)) # [('张三', 18), ('李四', 20), ('王五', 22)]

# # exec()
# # 执行简单的赋值语句
# code = "x = 10; y = 20; print(x + y)"
# exec(code)  #这里用 eval(code) 会报错
# #因为 exec 可以执行多个语句，而 eval 只能执行一个表达式
# # 执行函数定义
# function_code = """
# def add(a, b):
#     return a + b
# result = add(3, 5)
# print(result)
# """
# exec(function_code)
#
# #eval()
# str1 = "1 + 2"
# print(eval(str1))    #3
# str2 = "print('hello world')"
# eval(str2)    #hello world


# globals() 和 locals()

# #filter()
# #筛选出列表中所有偶数
# list1 = [1,2,3,4,5,6,7,8,9]
# re = filter(lambda x : x % 2 ==0, list1)
# print(list(re))    #[2, 4, 6, 8]
#
# # 判断列表中的那些数据是闰年
# list1 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
# is_even = lambda x : x % 400 == 0 or (x % 4 == 0 and x % 100 != 0)
# re = filter(is_even, list1)
# print(list(re))    #[2000, 2004, 2008]

# # reduce()
# from functools import reduce
#
# numbers = [1, 2, 3, 4, 5]
# # 提供初始值 10
# sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
# print(sum_with_initial)  # 输出: 25

# """
# 设可迭代对象就是list，实现my_filter() my_map() my_reduce()
# """
# # filter() 用于筛选数据
# def my_filter(func,lst):
#     for item in lst:
#         if not func(item):
#             lst.remove(item)
#     return lst
#
# # map() 用于对每个数据进行处理
# def my_map(func, lst):
#     for index in range(len(lst)):
#         lst[index] = func(lst[index])
#     return lst

# reduce() 用于对数据累积处理
# def my_reduce(func, lst, init = None):
#     # 如果提供了初始值，则将其作为累积结果的初始值
#     if not init:
#         result = init
#     else:
#         result = lst[0]
#     # 从列表的第二个元素开始累积处理
#     for index in range(1,len(lst)):   #错误，如果有初始值，则会跳过第一个元素
#         result = func(result, func(lst[index]))
#     return result

# # 修改
# def my_reduce(func, lst, init = None):
#     #处理空列表且无初始值的情况
#     if not lst and not init:
#         raise TypeError("reduce() of empty sequence with no initial value")
#     #如果提供了初始值，则将其作为累积结果的初始值
#     if init is not None:    # if not init 会把0也当作False
#         result = init
#         start_index = 0
#     else:
#         result = lst[0]
#         start_index = 1    #这样下面就可以用一样的逻辑处理了
#     for index in range(start_index, len(lst)):
#         # 累积逻辑
#         result = func(result, lst[index])
#
#     return result
#
#
# # 测试程序
# if __name__ == "__main__":
#     # 测试 my_filter()
#     nums = [1,2,3,4,5]
#     even_nums = my_filter(lambda x : x % 2 ==0, nums)
#     print(even_nums)    # [2, 4]
#
#     # 测试 my_map()
#     nums = [1,2,3,4,5]
#     squared_nums = my_map(lambda x : x * 2, nums)
#     print(squared_nums)    # [2, 4, 6, 8, 10]
#
#     # 测试 my_reduce()
#     nums = [1,2,3,4,5]
#     sum_nums = my_reduce(lambda x,y : x + y, nums, 100)
#     print(sum_nums)     # 115

#================================================================================


# Enclosing 作用域
# def outer_function():
#     enclosing_variable = 20  # 闭包变量
#     def inner_function():
#         print(enclosing_variable)
#     return inner_function
#
# outer_function()

# 如果内层函数想要修改外层函数的变量，需要使用 nonlocal 关键字
# def outer_function():
#     outer_variable = 10
#
#     def inner_function():
#         nonlocal outer_variable
#         outer_variable = 20  # 修改外层函数的变量
#         print(outer_variable)   # 20
#
#     inner_function()
#     print(outer_variable)  # 20
#
# outer_function()
#
# # Global 作用域
# global_variable = 30  # 全局变量
#
# def access_global():
#     print(global_variable)
#
# def modify_global():
#     global global_variable
#     global_variable = 40
#
# access_global()  # 输出 30
# modify_global()
# access_global()  # 输出 40


# # 函数的调用
# a = 100
# def func1():
#     print(a)
# def func2():
#     a = 200
#     func1()
# func2()  # 100

# 函数作为返回值
# def outer_function():
#     enclosing_variable = 20
#
#     def inner_function():
#         print(enclosing_variable)
#
#     return inner_function    #返回函数对象
#
# closure = outer_function()  # 调用 outer_function()，返回闭包函数
# closure() # 调用闭包函数，输出 20

def fun(n=None,o=None):
    print(o)
    return {"fun":lambda m:fun(m,n)}

a = fun(0)
a["fun"](1)
a["fun"](2)
a["fun"](3)

b = fun(0)["fun"](1)["fun"](2)["fun"](3)

c = fun(0)["fun"](1)
c["fun"](2)
c["fun"](3)

# # 递归结构
# def func1(a):
#     if a >= 5:
#         return 100  # 递归终止条件
#     else:
#         return a + func1(a + 1)  # 递归调用
#
# result = func1(1)
# print(result)   # 110
#
# #根据需求分析，如何设计递归函数
# # e.g. 求阶乘
# def func2(n):
#     if n == 1:
#         return 1  #递归终止条件：n=1时，阶乘为1
#     else:
#         return n * func2( n - 1 )   #递归调用，n! = n * (n-1)!
#
# result2 = func2(5)
# print(result2)   # 120

# 斐波那契数列： 从第三项开始，每一项都是前两项的和
# 第1项为0，第2项为1
# def fibonacci(n):
#     if n == 1:
#         return 0    #根据需求，第1项为0，第2项为1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)  #递归调用
# result = fibonacci(10)
# print(result)   # 34
#
# # 汉诺塔问题
# def hanni(n,a,b,c): #n盘子数，a起始柱，b辅助柱，c目标柱
#     if n == 1:
#         print(a + "->" + c)   #将最底下的盘子从A移动到C
#     else:
#         hanni(n-1,a,c,b)    #将n-1个盘子从A移动到B，C为辅助柱
#         print(a + "->" + c) # 将最底下的盘子从A移动到C
#         hanni(n-1,b,a,c)    #将n-1个盘子从B移动到C，A为辅助柱
# hanni(3,"A","B","C")

