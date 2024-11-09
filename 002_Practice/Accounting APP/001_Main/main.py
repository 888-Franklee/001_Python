import tkinter as tk

def click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("简单计算器")

# 显示框
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.SUNKEN)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    b = tk.Button(root, text=button, font="Arial 15", width=5, height=2)
    b.grid(row=row, column=col, padx=5, pady=5)
    b.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()












































































