import tkinter as tk
from tkinter import ttk
import pandas as pd

# 从 Excel 文件中读取中国省份及其城市数据
def load_province_data_from_excel(file_path):
    df = pd.read_excel(file_path)
    china_provinces = {}

    for _, row in df.iterrows():
        province = row['省份']
        city = row['城市']
        capital = row['省会']

        if province not in china_provinces:
            china_provinces[province] = {"省会": capital, "城市": []}

        china_provinces[province]["城市"].append(city)

    return china_provinces

# 加载数据
china_provinces = load_province_data_from_excel(r"D:\Lee Encyclopaedia（李論百科全書）\005_Information Tech\001_Python\Chinese City App\001_Main\China provinces.xlsx")

# 定义选择省份后的显示函数
def show_city_info(event):
    province = province_combobox.get()
    if province in china_provinces:
        capital = china_provinces[province]["省会"]
        cities = china_provinces[province]["城市"]
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"【省会】\n{capital}\n\n【城市】\n")
        for city in cities:
            output_text.insert(tk.END, f"{city}\n")

# 创建主窗口
root = tk.Tk()
root.title("中国省份与城市展示")

# 创建并放置标签和下拉框
tk.Label(root, text="选择省份", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
province_combobox = ttk.Combobox(root, values=list(china_provinces.keys()), font=("Arial", 14))
province_combobox.grid(row=0, column=1, padx=10, pady=10)
province_combobox.bind("<<ComboboxSelected>>", show_city_info)

# 创建并放置多行文本框
output_text = tk.Text(root, width=50, height=20, font=("Arial", 14))
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# 运行主循环
root.mainloop()
