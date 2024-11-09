import tkinter as tk
import calendar

def show_calendar():
    year = int(entry_year.get())
    month = int(entry_month.get())
    cal_text = calendar.month(year, month)
    label_result.config(text=cal_text)

root = tk.Tk()
root.title("日历查看器")

label_year = tk.Label(root, text="输入年份：", font=("Arial", 18))
label_year.pack(pady=10)

entry_year = tk.Entry(root, font=("Arial", 18))
entry_year.pack(pady=10)

label_month = tk.Label(root, text="输入月份：", font=("Arial", 18))
label_month.pack(pady=10)

entry_month = tk.Entry(root, font=("Arial", 18))
entry_month.pack(pady=10)

button = tk.Button(root, text="显示日历", font=("Arial", 18), command=show_calendar)
button.pack(pady=20)

label_result = tk.Label(root, text="", font=("Arial", 18), justify="left")
label_result.pack(pady=20)

root.mainloop()


