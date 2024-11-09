import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import datetime

# 读取Excel文件
def load_data():
    # 确保Excel文件路径正确
    file_path = r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Quick reference chart APP\001_Main\西暦和暦早見表.xlsx"
    data = pd.read_excel(file_path)

    # 修正列名去除空格或特殊字符
    data.columns = data.columns.str.strip()

    return data


# 计算年龄
def calculate_age(year):
    current_year = datetime.now().year
    return current_year - year

# 设置GUI窗口
def create_gui(data):
    root = tk.Tk()
    root.title('西暦和暦早見')

    # 创建一个Treeview来显示数据
    tree = ttk.Treeview(root, columns=('西暦', '和暦'), show='headings')
    tree.heading('西暦', text='西暦')
    tree.heading('和暦', text='和暦')

    # 填充Treeview
    for index, row in data.iterrows():
        tree.insert('', 'end', values=(row['西暦'], row['和暦']))

    # 当Treeview中的项目被选中时触发事件
    def on_tree_select(event):
        selection = tree.selection()
        if selection:
            item = tree.item(selection)
            selected_year = item['values'][0]
            corresponding_era = item['values'][1]
            age = calculate_age(selected_year)
            result_label.config(text=f'和暦: {corresponding_era}, 年龄: {age}岁')

    tree.bind('<<TreeviewSelect>>', on_tree_select)

    # 显示结果的标签
    result_label = tk.Label(root, text='', width=50)
    result_label.pack(pady=20)

    # 放置Treeview
    tree.pack(fill='both', expand=True)

    # 创建西暦输入框
    tk.Label(root, text="西暦:").pack(pady=5)
    year_entry = tk.Entry(root)
    year_entry.pack(pady=5)

    # 创建和暦输入框
    tk.Label(root, text="和暦:").pack(pady=5)
    era_entry = tk.Entry(root)
    era_entry.pack(pady=5)

    # 定义根据西暦显示和暦及年龄的功能
    def show_from_year():
        input_year = int(year_entry.get())
        result = data.loc[data['西暦'] == input_year]
        if not result.empty:
            corresponding_era = result.iloc[0]['和暦']
            age = calculate_age(input_year)
            result_label.config(text=f'和暦: {corresponding_era}, 年龄: {age}岁')
        else:
            result_label.config(text="未找到该西暦")

    # 定义根据和暦显示西暦及年龄的功能
    def show_from_era():
        input_era = era_entry.get()
        result = data.loc[data['和暦'] == input_era]
        if not result.empty:
            corresponding_year = result.iloc[0]['西暦']
            age = calculate_age(corresponding_year)
            result_label.config(text=f'西暦: {corresponding_year}, 年龄: {age}岁')
        else:
            result_label.config(text="未找到该和暦")

    # 添加按钮以执行查询
    tk.Button(root, text="西暦表示", command=show_from_year).pack(pady=5)
    tk.Button(root, text="查询表示", command=show_from_era).pack(pady=5)

    # 运行主循环
    root.mainloop()

# 主程序
def main():
    data = load_data()
    create_gui(data)

if __name__ == '__main__':
    main()
