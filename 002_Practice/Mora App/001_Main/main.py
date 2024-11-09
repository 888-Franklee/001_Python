import tkinter as tk
import random

def play(choice):
    options = ["石头", "剪刀", "布"]
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result = "平局！"
    elif (choice == "石头" and computer_choice == "剪刀") or \
         (choice == "剪刀" and computer_choice == "布") or \
         (choice == "布" and computer_choice == "石头"):
        result = "你赢了！"
    else:
        result = "你输了！"
    
    label_result.config(text=f"你选了：{choice}, 电脑选了：{computer_choice}\n{result}")

root = tk.Tk()
root.title("石头剪刀布游戏")

label = tk.Label(root, text="选择你的选项：", font=("Arial", 18))
label.pack(pady=10)

button_rock = tk.Button(root, text="石头", font=("Arial", 18), command=lambda: play("石头"))
button_rock.pack(pady=10)

button_scissors = tk.Button(root, text="剪刀", font=("Arial", 18), command=lambda: play("剪刀"))
button_scissors.pack(pady=10)

button_paper = tk.Button(root, text="布", font=("Arial", 18), command=lambda: play("布"))
button_paper.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 18))
label_result.pack(pady=20)

root.mainloop()

