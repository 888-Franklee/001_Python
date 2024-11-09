import tkinter as tk
from tkinter import filedialog, messagebox
from docx2pdf import convert
from pathlib import Path

# 定义确认按钮点击事件的函数
def confirm():
    word_folder = word_entry.get()
    pdf_folder = pdf_entry.get()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f'【Word保存場所】{word_folder}\n\n【PDF保存場所】{pdf_folder}\n\n以上でよろしいですか。\n問題がなければ、変換ボタンを押してください。')

# 定义转换按钮点击事件的函数
def convert_files():
    word_folder = Path(word_entry.get())
    pdf_folder = Path(pdf_entry.get())
    word_list = list(word_folder.glob("*.docx"))

    for w in word_list:
        convert(w, pdf_folder)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, '変換終了しました。ご確認ください。')

# 定义选择文件夹的函数
def browse_folder(entry):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)

# 创建主窗口
root = tk.Tk()
root.title('PDF変換ツール')

# 创建并放置标签和输入框
tk.Label(root, text='Wordの保存場所').grid(row=0, column=0, padx=10, pady=10)
word_entry = tk.Entry(root, width=80)
word_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text='参照', command=lambda: browse_folder(word_entry)).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text='PDFの保存場所').grid(row=1, column=0, padx=10, pady=10)
pdf_entry = tk.Entry(root, width=80)
pdf_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text='参照', command=lambda: browse_folder(pdf_entry)).grid(row=1, column=2, padx=10, pady=10)

# 创建并放置按钮
tk.Button(root, text='確認', command=confirm).grid(row=2, column=0, padx=10, pady=15)
tk.Button(root, text='変換', command=convert_files).grid(row=2, column=1, padx=10, pady=15)
tk.Button(root, text='終了', command=root.quit).grid(row=2, column=2, padx=10, pady=15)

# 创建并放置多行文本框
output_text = tk.Text(root, width=100, height=12)
output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# 运行主循环
root.mainloop()
