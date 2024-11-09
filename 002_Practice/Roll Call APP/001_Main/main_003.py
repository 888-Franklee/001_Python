import tkinter as tk  
from tkinter import messagebox, font  
import pandas as pd  
import random  
  
# 读取Excel文件并获取A列的人名  
def read_names_from_excel(file_path):  
    try:  
        df = pd.read_excel(file_path, engine='openpyxl')  
        names = df.iloc[:, 0].tolist()  # 使用iloc获取第一列（A列）  
        return names  
    except Exception as e:  
        print(f"Error reading Excel file: {e}")  
        return []  
  
# 随机选择一个获奖者  
def pick_winner(names):  
    if not names:  
        return None  
    winner = random.choice(names)  
    return winner  
  
# 显示获奖者  
def show_winner():  
    names = read_names_from_excel(r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Roll Call APP\001_Main\students.xlsx") 
    if not names:  
        messagebox.showerror("Error", "No names found in the Excel file.")  
        return  
    winner = pick_winner(names)  
    messagebox.showinfo("恭喜获奖者", f"恭喜！{winner} ")  
  
# 创建主窗口  
root = tk.Tk()  
root.title("精美抽奖App")  
root.geometry("400x200")  # 设置窗口大小  
root.configure(bg='lightblue')  # 设置背景颜色  
  
# 设置字体样式  
font_style = font.Font(family='Helvetica', size=14, weight='bold')  
  
# 创建一个标签来显示标题  
title_label = tk.Label(root, text="抽奖应用", font=font_style, bg='lightblue', fg='darkblue')  
title_label.pack(pady=20)  
  
# 创建一个按钮来触发抽奖  
draw_button = tk.Button(root, text="开始抽奖", command=show_winner, font=font_style, bg='green', fg='white', padx=20, pady=10)  
draw_button.pack(pady=20)  
  
# 运行主循环  
root.mainloop()