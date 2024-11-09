import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    listbox.delete(tk.ACTIVE)

root = tk.Tk()
root.title("待办事项清单")

label = tk.Label(root, text="任务：", font=("Arial", 18))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18))
entry.pack(pady=10)

button_add = tk.Button(root, text="添加任务", font=("Arial", 18), command=add_task)
button_add.pack(pady=10)

button_delete = tk.Button(root, text="删除选中的任务", font=("Arial", 18), command=delete_task)
button_delete.pack(pady=10)

listbox = tk.Listbox(root, font=("Arial", 18))
listbox.pack(pady=20)

root.mainloop()

