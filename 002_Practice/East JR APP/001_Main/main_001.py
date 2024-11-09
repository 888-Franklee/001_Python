import tkinter as tk
from tkinter import ttk

# 東日本JRの主要路線とその駅リスト（サンプルデータ）
jr_east_lines = {
    "山手線": ["東京", "品川", "渋谷", "新宿", "池袋", "上野"],
    "中央線": ["東京", "神田", "御茶ノ水", "四ツ谷", "新宿", "中野", "立川"],
    "京浜東北線": ["大宮", "浦和", "赤羽", "上野", "東京", "品川", "横浜"],
    "総武線": ["千葉", "船橋", "錦糸町", "秋葉原", "新宿", "中野"],
    "常磐線": ["上野", "北千住", "松戸", "柏", "取手", "土浦"],
    "埼京線": ["大宮", "赤羽", "池袋", "新宿", "渋谷", "大崎"]
}

# 駅を表示する関数
def show_stations(event):
    selected_line = line_listbox.get(line_listbox.curselection())  # 選択された路線を取得
    stations_listbox.delete(0, tk.END)  # 駅のリストをクリア
    stations = jr_east_lines.get(selected_line, [])
    for station in stations:
        stations_listbox.insert(tk.END, station)  # 駅をリストボックスに追加

# メインウィンドウの設定
root = tk.Tk()
root.title("JR東日本 路線選択アプリ")
root.geometry("400x300")

# フレームの作成
frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

# ラベル
label = tk.Label(frame, text="JR東日本の路線を選んでください")
label.pack()

# 路線リストボックス
line_listbox = tk.Listbox(frame, height=6)
line_listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# 路線をリストボックスに表示
for line in jr_east_lines.keys():
    line_listbox.insert(tk.END, line)

# 駅のリストボックス
stations_listbox = tk.Listbox(frame, height=6)
stations_listbox.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# 路線選択時に駅を表示する
line_listbox.bind("<<ListboxSelect>>", show_stations)

# アプリケーションの実行
root.mainloop()
