import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("滚动条")
root.geometry("300x200")

# 创建文本框和滚动条
text = tk.Text(root, wrap=tk.WORD)
scrollbar = tk.Scrollbar(root, command=text.yview)
text.configure(yscrollcommand=scrollbar.set)

# 布局管理
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 插入一些文本
for i in range(1, 101):
    text.insert(tk.END, f"这是一行测试文本 {i}\n")

# 运行主循环
root.mainloop()