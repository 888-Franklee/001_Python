import random

#基本用法：
print(random.randrange(1, 10))#这将返回一个1到9之间的随机整数（包含1但不包含10）

#指定步长：
print(random.randrange(1, 10, 2))#这将返回一个1到9之间的随机整数，但只会是奇数（因为步长为2，生成的数字序列为1, 3, 5, 7, 9）

#步长影响:
random.randrange(1, 10, 3)#步长影响：如果指定了步长step，则生成的随机数会从start开始，每次增加step，直到小于stop。例如，random.randrange(1, 10, 3)只会生成1, 4, 7

#步长为负数:
print(random.randrange(10, 1, -2))#这将返回一个10到2之间，每隔2个数的随机整数，可能的值有：10, 8, 6, 4, 2。

#只指定结束值:
print(random.randrange(10))#这将返回一个0到9之间的随机整数（不包含10），相当于random.randrange(0, 10)

#详细示例:
result = random.randrange(10, 50, 5)
print(result)#可能的输出值包括：10, 15, 20, 25, 30, 35, 40, 45

#异常处理:
#参数不合法：如果start大于stop且步长为正数，或者start小于stop且步长为负数，会引发ValueError
#步长为零：如果步长为零，也会引发ValueError，因为步长为零无意义