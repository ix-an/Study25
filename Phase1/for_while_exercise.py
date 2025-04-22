"""
假设一个用户信息如下:
 用户名是:root
 密码是: 123456
写一个身份验证的程序，让用户输入用户名和密码登录, 用户名和密码全部匹配，提示登录成功。
否则继续，最多尝试3次。3次不匹配以后提示登录失败.
"""
# USER_NAME = "root"
# PASS_WORD = "123456"
# for i in range(3):
#     user_name = input("请输入用户名：")
#     pass_word = input("请输入密码：")
#     if user_name == USER_NAME and pass_word == PASS_WORD:
#         print("登录成功！")
#         break
#     else:
#         print("用户或密码错误，请重试")
# else:
#     print("3次不成功！登录失败！")

"""
写一个程序, 用列表保存用户输入的数据
1. 让用户输入4个任意的整数，放入列表
2. 在第三个整数前面插入一个100
3. 删除列表中的第4个整数
4. 将之前输入的第二个整数加上1 后放回原处
5. 打印现在的列表
"""
# list1 = []
# for i in range(4):
#     num = int(input("请输入一个整数："))
#     list1.append(num)
# list1.insert(2, 100)
# del list1[3]
# list1[1] += 1
# print(list1)

"""
写一个程序，输入一段文字，
1) 写程序计算出文字中，每个字出现的次数，
2) 求出 这段文字中字符的个数
如: 我喜欢你，你不喜欢我
'我': 2
'你': 2
'喜': 2
'欢': 2
'，': 1
'不': 1
您输入的这段文字有 6 种字符
"""
# str1 = input("请输入一段文字：")
# set1 = set(str1)
# for i in set1:
#     count = 0
#     for j in str1:
#         if i == j:
#             count += 1
#     print(f"\'{i}\' 在这段文字中出现了 {count} 次")
# print("您输入的这段文字有" + str(len(set1)) + "种字符")

# str.count() 可以直接统计字符出现的次数
# str1 = input("请输入一段文字：")
# set1 = set(str1)
# for item in set1:
#     print(f"\'{item}\' 在这段文字中出现了 {str1.count(item)} 次")
# print("您输入的这段文字有" + str(len(set1)) + "种字符")


"""
写程序, 输入一个整数n，打印 宽度为n 的空心正方形
"""
# n = int(input("请输入一个整数："))
# #第一行
# print("#" * n)
# #中间行
# for i in range(n-2):
#     print("#" + " " * (n-2) + "#")
# #最后一行
# print("#" * n)

"""
写一个程序，输入任意行文字，当输入为空字符串时结束输入，将所有的字符串以最长的字符串宽度打印如下方框
请输入: hello
请输入: hello world
请输入: <回车输入结束>
+-------------+
|    hello    |
| hello world |
+-------------+
"""
# str_length = 0
# list_str = []
# #记录数据
# while True:
#     str1 = input("请输入：")
#     if str1 == "":      # if not str1: 效果相同
#         print("<回车输入结束>")
#         break
#     list_str.append(str1)
#     if len(str1) > str_length:
#         str_length = len(str1)
# #格式化输出
# print("+" + "-" * (str_length+2) + "+")
# # for s in list_str:
# #     left_space = (str_length - len(s)) // 2 + 1
# #     right_space = (str_length - len(s)) - left_space + 2
# #     print("|" + " " * left_space + s + " " * right_space + "|")
# """
# str.center() 可以直接居中输出
# for s in list_str:
#     print("|" + s.center(str_length+2) + "|")
# """
# for s in list_str:
#     print("|" + s.center(str_length + 2) + "|")
# print("+" + "-" * (str_length+2) + "+")


"""
算出 100 ~ 999 的水仙花数
水仙花数是 指百位的3次方 + 十位的3次方  + 各位的3次方  等于原数的数
打印出所有的 水仙花数
"""
# for i in range(100, 1000):
#     hundreds = i // 100
#     tens = i % 100 // 10
#     ones = i % 10
#     narcissus = hundreds ** 3 + tens ** 3 + ones ** 3
#     if i == narcissus:
#         print(i)

"""
打印 九九 乘法表
1x1=1
1x2=2 2x2=4
1x3=3 2x3=6 3x3=9
....
1x9=9 ........ 9x9=81
"""
# # i 对应乘号右边，j 对应乘号左边
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{j} x {i} = {j * i}",end="\t")
#         if i == j:
#             print()
#             break