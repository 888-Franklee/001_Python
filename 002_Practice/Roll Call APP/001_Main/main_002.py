import tkinter as tk
from tkinter import ttk
import random
import openpyxl
import os

# 从Excel读取学生名单，包含性别
def load_students(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        result_label.config(text="学生名单文件不存在！")
        return []

    try:
        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active
        students = []
        for row in sheet.iter_rows(min_row=2, max_col=3, values_only=True):
            student_name = row[1]  # 假设B列是学生姓名
            gender = row[2]  # 假设C列是性别（"男" 或 "女"）
            if student_name and gender:
                students.append({"name": student_name, "gender": gender})
        return students
    except Exception as e:
        result_label.config(text=f"读取学生名单时出错: {str(e)}")
        return []

# 根据性别筛选学生并随机选择一个
def pick_student(gender=None):
    if students:
        if gender:
            filtered_students = [s['name'] for s in students if s['gender'] == gender]
        else:
            filtered_students = [s['name'] for s in students]  # 不限制性别

        if filtered_students:
            selected_student = random.choice(filtered_students)
            result_label.config(text=f"请 {selected_student} 回答问题！")
        else:
            result_label.config(text=f"没有符合条件的学生！")
    else:
        result_label.config(text="学生名单为空！")

# 创建主窗口
root = tk.Tk()
root.title("点名APP")
root.geometry("400x400")
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
pick_all_button = ttk.Button(root, text="随机点名（男女）", command=lambda: pick_student())
pick_all_button.pack(pady=10)

pick_boys_button = ttk.Button(root, text="随机点名（男生）", command=lambda: pick_student("男"))
pick_boys_button.pack(pady=10)

pick_girls_button = ttk.Button(root, text="随机点名（女生）", command=lambda: pick_student("女"))
pick_girls_button.pack(pady=10)

# 显示选中的学生
result_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#F0F8FF", fg="#000000")
result_label.pack(pady=20)

# 运行应用
root.mainloop()
