import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("记事本")

text = tk.Text(root, font=("Arial", 14))
text.pack(expand=True, fill=tk.BOTH)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="新建", command=new_file)
file_menu.add_command(label="打开", command=open_file)
file_menu.add_command(label="保存", command=save_file)
menu_bar.add_cascade(label="文件", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()
