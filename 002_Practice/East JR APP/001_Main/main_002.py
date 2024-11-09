import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Ekispert APIの設定
API_KEY = "あなたのAPIキー"  # Ekispert APIのAPIキーをここに入力してください
LINE_ENDPOINT = "http://api.ekispert.jp/v1/json/operationLine"
STATION_ENDPOINT = "http://api.ekispert.jp/v1/json/station"

# APIキーの確認関数
def check_api_key():
    if API_KEY == "あなたのAPIキー" or not API_KEY:
        messagebox.showerror("エラー", "APIキーが設定されていません。APIキーを入力してください。")
        return False
    return True

# 路線データを取得する関数
def get_lines():
    if not check_api_key():
        return []
    
    params = {
        "key": API_KEY,
    }
    try:
        response = requests.get(LINE_ENDPOINT, params=params)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        data = response.json()
        return data.get('ResultSet', {}).get('Line', [])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("エラー", f"路線情報の取得に失敗しました。\n{e}")
        return []

# 駅データを取得する関数
def get_stations(line_name):
    if not check_api_key():
        return []
    
    params = {
        "key": API_KEY,
        "name": line_name
    }
    try:
        response = requests.get(STATION_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get('ResultSet', {}).get('Point', [])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("エラー", f"駅情報の取得に失敗しました。\n{e}")
        return []

# 路線が選択されたときに駅を表示する関数
def on_line_selected(event):
    selection = line_listbox.curselection()
    if not selection:  # 選択されていない場合は何もしない
        return
    selected_line = line_listbox.get(selection)
    stations = get_stations(selected_line)
    station_listbox.delete(0, tk.END)  # 前回の駅データをクリア
    for station in stations:
        station_name = station['Station']['Name']
        station_listbox.insert(tk.END, station_name)

# メインウィンドウの作成
root = tk.Tk()
root.title("JR東日本 路線・駅情報")

# 路線リストのフレーム
frame_lines = tk.Frame(root)
frame_lines.pack(side=tk.LEFT, padx=10, pady=10)

# 路線リストのタイトル
line_label = tk.Label(frame_lines, text="JR東日本 路線一覧", font=("Helvetica", 16))
line_label.pack(pady=10)

# 路線リストボックス
line_listbox = tk.Listbox(frame_lines, height=20, width=40)
line_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# スクロールバー
line_scrollbar = tk.Scrollbar(frame_lines)
line_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
line_listbox.config(yscrollcommand=line_scrollbar.set)
line_scrollbar.config(command=line_listbox.yview)

# 駅リストのフレーム
frame_stations = tk.Frame(root)
frame_stations.pack(side=tk.RIGHT, padx=10, pady=10)

# 駅リストのタイトル
station_label = tk.Label(frame_stations, text="駅一覧", font=("Helvetica", 16))
station_label.pack(pady=10)

# 駅リストボックス
station_listbox = tk.Listbox(frame_stations, height=20, width=40)
station_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# スクロールバー
station_scrollbar = tk.Scrollbar(frame_stations)
station_scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
station_listbox.config(yscrollcommand=station_scrollbar.set)
station_scrollbar.config(command=station_listbox.yview)

# 路線が選択されたらon_line_selectedを呼び出す
line_listbox.bind('<<ListboxSelect>>', on_line_selected)

# 路線情報のロード
lines = get_lines()
for line in lines:
    line_name = line['Name']
    line_listbox.insert(tk.END, line_name)

# アプリケーションを実行
root.mainloop()
