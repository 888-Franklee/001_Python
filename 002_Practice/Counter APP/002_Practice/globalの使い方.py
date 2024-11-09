x = 10  # 全局变量

def modify_global():
    global x  # 声明x为全局变量
    x = 20  # 修改全局变量的值

print(f"修改前的x: {x}")
modify_global()
print(f"修改后的x: {x}")

def create_global():
    global y  # 声明y为全局变量
    y = 30  # 创建并初始化全局变量

create_global()
print(f"新的全局变量y: {y}")

count = 0  # 全局变量

def increment():
    global count  # 声明count为全局变量
    count += 1  # 增加全局变量的值

def reset():
    global count  # 声明count为全局变量
    count = 0  # 重置全局变量的值

print(f"初始count: {count}")
increment()
increment()
print(f"increment两次后的count: {count}")
reset()
print(f"reset后的count: {count}")

num = 100  # 全局变量

def outer_function():
    def inner_function():
        global num  # 声明num为全局变量
        num = 200  # 修改全局变量的值
    inner_function()

print(f"修改前的num: {num}")
outer_function()
print(f"修改后的num: {num}")

x = 10  # 全局变量

#尽量避免使用 global，因为它会使代码难以理解和维护。可以通过返回值和参数传递来实现相同的功能

def modify(x):
    return 20  # 返回新的值

print(f"修改前的x: {x}")
x = modify(x)
print(f"修改后的x: {x}")