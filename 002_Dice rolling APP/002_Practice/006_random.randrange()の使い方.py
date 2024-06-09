import random

#指定步长：
print(random.randrange(1, 10, 2))#这将返回一个1到9之间的随机整数，但只会是奇数（因为步长为2，生成的数字序列为1, 3, 5, 7, 9）

#只指定结束值:
print(random.randrange(10))