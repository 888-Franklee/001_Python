#sg.Button(button_text='Button', button_color=None, key=None, tooltip=None, **kwargs)
#button_text：按钮上显示的文本，默认为 "Button"。
#button_color：按钮的颜色，格式为 (按钮颜色, 文本颜色)，例如 ('red', 'white')。
#key：按钮的唯一标识符，用于在事件循环中识别该按钮。
#tooltip：按钮的提示文本，当鼠标悬停在按钮上时显示。
#**kwargs：其他可选参数，用于进一步定制按钮的属性。
#size：按钮的大小，格式为 (宽度, 高度)，例如 size=(10, 1)。
#font：按钮的字体，例如 font=('Helvetica', 12)。
#disabled：是否禁用按钮，设置为 True 则按钮不可点击。
#visible：是否显示按钮，设置为 False 则按钮不可见。

import PySimpleGUI as sg

# 定义窗口布局
layout = [
    [sg.Button('确定', size=(18,1), key='-OK-', button_color=('white', 'green'), tooltip='点击确定')],
    [sg.Button('取消', size=(18,1), key='-CANCEL-', button_color=('white', 'red'), tooltip='点击取消')],
    [sg.Button('帮助', size=(18,1), key='-HELP-', button_color=('white', 'blue'), tooltip='点击获取帮助')],
    [sg.Button('禁用按钮', size=(18,1), key='-DISABLED-', disabled=True)],
    [sg.Button('隐藏按钮', size=(18,1), key='-HIDDEN-', visible=False)],
    [sg.Button('显示隐藏按钮', size=(18,1), key='-SHOW-')]
]

# 创建窗口
window = sg.Window('按钮示例', layout,size=(300,200))

# 事件循环
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-OK-':
        sg.popup('你点击了确定按钮')
    elif event == '-CANCEL-':
        sg.popup('你点击了取消按钮')
    elif event == '-HELP-':
        sg.popup('你点击了帮助按钮')
    elif event == '-SHOW-':
        window['-HIDDEN-'].update(visible=True)

# 关闭窗口
window.close()