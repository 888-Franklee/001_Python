import tkinter as tk
from tkinter import ttk
import random

# 定义生成随机数的函数
def dice(max_value):
    max_val = int(max_value)
    return str(random.randint(1, max_val))

# 定义执行按钮点击事件的函数
def execute():
    max_value = entry.get()
    if max_value.isdigit() and int(max_value) > 0:
        result = dice(max_value)
        text_box.insert(tk.END, result + "\n")
    else:
        text_box.insert(tk.END, "请输入有效的数字\n")

# 创建主窗口
root = tk.Tk()
root.title("1~最大值的骰子")

# 创建并放置标签和输入框
label = tk.Label(root, text="数字を入力してください", font=("None", 14))
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, font=("None", 14))
entry.grid(row=0, column=1, padx=10, pady=10)

# 创建并放置按钮
button = tk.Button(root, text="実行", font=("None", 14), command=execute)
button.grid(row=1, column=0, columnspan=2, pady=15)

# 创建并放置多行文本框
text_box = tk.Text(root, width=60, height=10, font=("None", 14))
text_box.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 绑定回车键事件
root.bind('<Return>', lambda event: execute())

# 运行主循环
root.mainloop()
