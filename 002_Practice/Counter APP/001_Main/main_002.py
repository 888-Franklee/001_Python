import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("计数器")
root.geometry("300x200")

# 初始计数值
count = 0

# 创建标签显示计数值
label = tk.Label(root, text="计数值: 0")
label.pack()

# 增加计数的函数
def increase_count():
    global count
    count += 1
    label.config(text=f"计数值: {count}")

# 减少计数的函数
def decrease_count():
    global count
    count -= 1
    label.config(text=f"计数值: {count}")

# 创建增加计数的按钮
increase_button = tk.Button(root, text="增加", command=increase_count)
increase_button.pack()

# 创建减少计数的按钮
decrease_button = tk.Button(root, text="减少", command=decrease_count)
decrease_button.pack()

# 运行主循环
root.mainloop()

