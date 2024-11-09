import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import configparser
import os

def save_config(year, month, day, hour, minute, folder_path):
    # 格式化时间为文件名
    selected_time = f"{year}-{month:02d}-{day:02d}_{hour:02d}-{minute:02d}"
    config_filename = f"{selected_time}.ini"
    config_filepath = os.path.join(folder_path, config_filename)

    # 创建配置对象
    config = configparser.ConfigParser()
    config['SelectedTime'] = {
        'Year': year,
        'Month': month,
        'Day': day,
        'Hour': hour,
        'Minute': minute
    }

    # 保存配置文件
    with open(config_filepath, 'w') as configfile:
        config.write(configfile)
    
    messagebox.showinfo("保存成功", f"配置文件已保存为 {config_filepath}")

def generate_config():
    year = int(year_var.get())
    month = int(month_var.get())
    day = int(day_var.get())
    hour = int(hour_var.get())
    minute = int(minute_var.get())
    folder_path = folder_var.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("错误", "无效的文件夹路径")
        return

    save_config(year, month, day, hour, minute, folder_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    folder_var.set(folder_path)

# 创建主窗口
root = tk.Tk()
root.title("选择年月日时间")
root.geometry("400x400")

# 创建年份选择器
tk.Label(root, text="年份:").pack()
year_var = tk.StringVar()
year_combobox = ttk.Combobox(root, textvariable=year_var)
year_combobox['values'] = [str(year) for year in range(1900, 2101)]
year_combobox.current(datetime.now().year - 1900)
year_combobox.pack()

# 创建月份选择器
tk.Label(root, text="月份:").pack()
month_var = tk.StringVar()
month_combobox = ttk.Combobox(root, textvariable=month_var)
month_combobox['values'] = [f"{month:02d}" for month in range(1, 13)]
month_combobox.current(datetime.now().month - 1)
month_combobox.pack()

# 创建日期选择器
tk.Label(root, text="日期:").pack()
day_var = tk.StringVar()
day_combobox = ttk.Combobox(root, textvariable=day_var)
day_combobox['values'] = [f"{day:02d}" for day in range(1, 32)]
day_combobox.current(datetime.now().day - 1)
day_combobox.pack()

# 创建小时选择器
tk.Label(root, text="小时:").pack()
hour_var = tk.StringVar()
hour_combobox = ttk.Combobox(root, textvariable=hour_var)
hour_combobox['values'] = [f"{hour:02d}" for hour in range(0, 24)]
hour_combobox.current(datetime.now().hour)
hour_combobox.pack()

# 创建分钟选择器
tk.Label(root, text="分钟:").pack()
minute_var = tk.StringVar()
minute_combobox = ttk.Combobox(root, textvariable=minute_var)
minute_combobox['values'] = [f"{minute:02d}" for minute in range(0, 60)]
minute_combobox.current(datetime.now().minute)
minute_combobox.pack()

# 创建文件夹路径输入框
tk.Label(root, text="选择保存文件夹:").pack()
folder_var = tk.StringVar()
folder_entry = tk.Entry(root, textvariable=folder_var, width=50)
folder_entry.pack()

# 创建选择文件夹按钮
folder_button = tk.Button(root, text="浏览", command=select_folder)
folder_button.pack()

# 创建生成配置文件按钮
tk.Button(root, text="生成配置文件", command=generate_config).pack(pady=20)

# 运行主循环
root.mainloop()


