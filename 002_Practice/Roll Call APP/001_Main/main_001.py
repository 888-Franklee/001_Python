import tkinter as tk
from tkinter import ttk
import random
import openpyxl
import os

# 从Excel读取学生名单
def load_students(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        result_label.config(text="学生名单文件不存在！")
        return []

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        students = []
        for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
            student_name = row[1]  # 假设B列是学生姓名
            if student_name:
                students.append(student_name)
        return students
    except Exception as e:
        result_label.config(text=f"读取学生名单时出错: {str(e)}")
        return []

# 随机选择一个学生
def pick_student():
    if students:
        selected_student = random.choice(students)
        result_label.config(text=f"请 {selected_student} 回答问题！")
    else:
        result_label.config(text="学生名单为空！")

# 创建主窗口
root = tk.Tk()
root.title("点名APP")
root.geometry("400x300")
root.config(bg="#F0F8FF")  # 设置背景色

# 定义样式
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), padding=10, background="#4682B4")
style.configure("TLabel", font=("Helvetica", 20), padding=10)

# 加载Excel中的学生数据
students = load_students(r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Roll Call APP\001_Main\students.xlsx")  # 请将文件路径改为你的Excel路径

# 标题标签
title_label = tk.Label(root, text="欢迎使用随机点名APP", font=("Helvetica", 24, "bold"), bg="#F0F8FF", fg="#4682B4")
title_label.pack(pady=20)

# 创建按钮和显示区域
pick_button = ttk.Button(root, text="随机点名", command=pick_student)
pick_button.pack(pady=20)

# 显示选中的学生
result_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#F0F8FF", fg="#000000")
result_label.pack(pady=20)

# 运行应用
root.mainloop()
