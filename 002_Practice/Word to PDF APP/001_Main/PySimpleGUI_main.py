import PySimpleGUI as sg
from docx2pdf import convert
from pathlib import Path

layout = [[sg.Text('Wordの保存場所'), sg.Input(key='-word-',size=(100,1))],
          [sg.Text('PDFの保存場所 '), sg.Input(key='-pdf-',size=(100,1))],
          [sg.Button('確認'), sg.Button('変換'),sg.Button('終了')],
          [sg.Output(size=(120,12), key='-OUTPUT-')]
         ]

window = sg.Window('PDF変換ツール', layout, size=(600, 300))

while True:
    event, values = window.read()
    
    word_folder=Path(values["-word-"])
    pdf_folder=Path(values["-pdf-"])
    word_list = list(word_folder.glob("*.docx"))
    
    if event == sg.WIN_CLOSED or event == '終了':
        break
    elif event == '確認':
        window['-OUTPUT-'].update(f'【Word保存場所】{values["-word-"]} \n \n【PDF保存場所】{values["-pdf-"]}\n \n以上でよろしいですか。\n問題がなければ、確定ボタンを押してください。')
    elif event == '変換':
        for w in word_list:
            convert(w, pdf_folder)
        window['-OUTPUT-'].update(f'変換終了しました。ご確認ください。')
    
window.close()













































































