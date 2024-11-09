import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("计数器")
root.geometry("300x200")

# 初始计数值
count = 0

# 创建标签显示计数值
label = tk.Label(root, text="计数值: 0")
label.pack(pady=20)

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

# 创建一个框架来包含按钮
button_frame = tk.Frame(root)
button_frame.pack()

# 创建增加计数的按钮
increase_button = tk.Button(button_frame, text="增加", command=increase_count)
increase_button.pack(side=tk.LEFT, padx=10)

# 创建减少计数的按钮
decrease_button = tk.Button(button_frame, text="减少", command=decrease_count)
decrease_button.pack(side=tk.LEFT, padx=10)

# 运行主循环
root.mainloop()
