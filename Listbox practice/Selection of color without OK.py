
#!usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg

#　リストボックスに表示するデータ
choices = ('赤', '緑', '青', '黄色', 'オレンジ', '紫', '黒')

#　レイアウト（1段目：テキスト、2段目：リストボックス）
layout = [  [sg.Text('　あなたの好きな色はなんですか？　')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True)] ]


#　ウィンドウ生成
window = sg.Window('リストボックスアプリ', layout)

while True:
    #　イベント読み取り
    event, values = window.read()

    #　ウィンドウ右上の×を押したときの処理
    if event == sg.WIN_CLOSED:
        break

    #　リストから色が選択されたときの処理
    if values['-COLOR-']:
        #　ポップアップを表示
        sg.popup(f"　あなたの好きな色は{values['-COLOR-'][0]}ですね。　")

window.close()