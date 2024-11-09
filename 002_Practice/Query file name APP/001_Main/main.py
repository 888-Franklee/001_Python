import os
import tkinter as tk
from tkinter import filedialog, Listbox, Scrollbar, Radiobutton, StringVar

# 创建主窗口
root = tk.Tk()
root.title("文件类型查看器")
root.geometry("600x500")

# 定义函数用于选择文件夹
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        show_files(folder_path, file_type.get())

# 递归获取所有子文件夹中的指定类型文件，并只显示文件名
def show_files(folder, extension):
    file_listbox.delete(0, tk.END)  # 清空文件列表
    unique_files = set()  # 使用集合来避免重复文件名
    for dirpath, _, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                unique_files.add(filename)  # 只添加文件名，不包括路径

    for filename in sorted(unique_files):  # 按字母排序显示文件名
        file_listbox.insert(tk.END, filename)

# 标签显示选择的文件夹路径
folder_label = tk.Label(root, text="请选择一个文件夹", wraplength=500)
folder_label.pack(pady=10)

# 创建一个按钮用于选择文件夹
select_button = tk.Button(root, text="选择文件夹", command=select_folder)
select_button.pack(pady=10)

# 文件类型选择：PDF 或 Word
file_type = StringVar()
file_type.set(".pdf")  # 默认选择PDF

pdf_radiobutton = Radiobutton(root, text="PDF文件", variable=file_type, value=".pdf")
pdf_radiobutton.pack()

word_radiobutton = Radiobutton(root, text="Word文件", variable=file_type, value=".docx")
word_radiobutton.pack()

# 滚动条和列表框用于显示文件名
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

file_listbox = Listbox(root, width=80, height=20, yscrollcommand=scrollbar.set)
file_listbox.pack(pady=10)

scrollbar.config(command=file_listbox.yview)

# 运行主循环
root.mainloop()
