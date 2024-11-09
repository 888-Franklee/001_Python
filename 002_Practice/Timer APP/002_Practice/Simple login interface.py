import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.title("登录界面")
root.geometry("300x200")

# 用户名标签和输入框
tk.Label(root, text="用户名:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

# 密码标签和输入框
tk.Label(root, text="密码:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# 登录按钮点击事件处理函数
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "user" and password == "pass":
        messagebox.showinfo("提示", "登录成功")
    else:
        messagebox.showerror("错误", "用户名或密码错误")

# 创建登录按钮
login_button = tk.Button(root, text="登录", command=login)
login_button.pack()

# 运行主循环
root.mainloop()