"""
1.编写一个程序，要求用户输入两个整数，
然后计算并打印这两个数的和、差、积和商（注意除法运算时避免除以零错误）。
"""
# try:
#     a = int(input("请输入第一个整数："))
#     b = int(input("请输入第二个整数："))
# except Exception as e:
#     print(e)  # 若输入无法转换为整数，则打印错误信息
# else:
#     # 和、差、积
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     # 商需要判断除数是否为零
#     if b != 0:
#         print(a / b)
#     else:
#         print("除数不能为零")

"""
2.设计一个名为`reverse_string`的函数，接受一个字符串作为参数，并返回其反转后的字符串。
"""
# def reverse_string(string):
#     return string[::-1]

"""
3. 实现一个斐波那契数列生成器函数，该函数接受一个整数n作为参数，返回前n项斐波那契数列。
"""
# def fibonacci(n):
#     result = []
#     a, b = 0, 1
#     #如果输入的不是整数
#     try:
#         n = int(n)
#     except ValueError:
#         print("请输入一个整数")
#         return []
#     # 如果输入的是负数，则返回空列表
#     if n < 0:
#         print("请输入一个正整数")
#         return result
#     # 如果输入的是0，则返回[]
#     elif n == 0:
#         return result
#     # 输入的是正整数，则返回前n项斐波那契数列
#     for _ in range(n):
#         result.append(a)
#         a, b = b, a + b
#     return result


"""
4. 编写一个Python类`Person`，包含属性姓名(name)、年龄(age)和地址(address)，
并实现一个方法`introduce_self`，用于打印个人的基本信息。
"""
# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def introduce_self(self):
#         print(f"{self.name}的年龄为{self.age}，家住{self.address}")


"""
5. 使用列表推导式生成一个列表，该列表包含从1到100的所有奇数的平方。
"""
# lst = [i ** 2 for i in range(1, 101) if i % 2 != 0]

"""
6. 使用正则将字符串” python is    easy  to  learn”中的每个单词全部提取出来,
放在列表中,并将每一个单词的码值和计算出来装在另外一个列表中 
"""
# import re
# data = "python is    easy  to  learn"
# # 提取单词
# words_list = re.findall(r"\w+", data)
#
# # 计算每个单词的码值和，并装在另一个列表中
# code_list = []
# for word in words_list:
#     code_sum = 0
#     for char in word:
#         code = ord(char)
#         code_sum += code
#     code_list.append(code_sum)


"""
7.使用正则将字符串”  18282832341  ”中首尾空白字符去掉,并将前面的空白替换为”+0800-”
"""
# import re
# number = "  18282832341  "
# # 替换开头的空白
# number = re.sub(r"^\s+", "+0800-", number)
# # 替换结尾的空白
# number = re.sub(r"\s+$", "", number)

"""
8. 使用Python的NumPy库，创建一个形状为(4,4)的二维数组，并且初始化所有元素为其行索引与列索引之和。
"""
# import numpy as np
# # 创建数组
# arr = np.zeros(shape=(4,4))
# print(arr)
# # 替换元素值
# for i in range(4):
#     for j in range(4):
#         arr[i][j] = i + j

"""
9. 使用Python的Pandas库，创建一个DataFrame对象，包含三列：
'Name'、'Age'和'Gender'，
数据分别为['Alice', 'Bob', 'Charlie'], [25, 30, 35]和['Female', 'Male', 'Male']，
并计算所有人的平均年龄。
"""
# import pandas as pd
# # 创建对象
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'Gender': ['Female', 'Male', 'Male']
# }
# df = pd.DataFrame(data)
#
# # 计算所有人的平均年龄
# avg_age = df['Age'].mean()


"""
10.假设你有一个包含员工信息的CSV文件employees.csv，
其中包含以下列：EmployeeID（员工编号）、Name（姓名）、Department（部门）、Salary（薪资）。
数据文件内容（employees.csv）：
EmployeeID,Name,Department,Salary
1,John Doe,Finance,70000
2,Jane Smith,Marketing,65000
3,Bob Johnson,Finance,80000
4,Alice Brown,IT,75000
5,Mike Davis,Marketing,72000

要求：
1.使用Pandas读取employees.csv文件，并创建一个DataFrame。
2.计算每个部门的平均薪资，并按平均薪资从高到低排序。
3.找出薪资超过其所在部门平均薪资的员工，并创建一个新的DataFrame。
4.将结果保存到一个新的CSV文件above_average_salaries.csv中。
"""
import pandas as pd
# 读取文件并创建DataFrame
df = pd.read_csv("../CSV/employees.csv")

# 计算每个部门的平均薪资并降序排序
df["DeptAvg"] = df.groupby("Department")["Salary"].transform("mean")
df.sort_values("DeptAvg", ascending=False, inplace=True)

# 找出薪资超过其所在部门平均薪资的员工,并放入一个新的DataFrame
df_above_avg = df[df["Salary"] > df["DeptAvg"]]

# 将结果保存到一个新的CSV文件
df_above_avg.to_csv("above_average_salaries.csv", index=False)

