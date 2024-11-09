#sg.Input(default_text='', size=(None, None), password_char='', key=None, **kwargs)
#default_text：输入框的默认文本，默认为空字符串。
#size：输入框的大小，以字符数为单位。格式为(宽度, 高度)。
#password_char：如果设置了该参数，则输入框会以密码模式显示字符，所有输入的字符都会显示为指定的字符（例如*）。
#key：输入框的唯一标识符，用于在事件循环中访问输入框的值。
#**kwargs：其他可选参数，用于进一步定制输入框的属性。
#常见的 **kwargs 参数
#background_color：设置输入框的背景颜色。
#text_color：设置输入框中的文本颜色。
#font：设置输入框中的字体，例如font=('Helvetica', 12)。
#tooltip：设置输入框的提示文本，当鼠标悬停在输入框上时显示。

import PySimpleGUI as sg

# 定义窗口布局
layout = [
    [sg.Text('请输入用户名：')],
    [sg.Input(key='-USERNAME-', size=(40, 1), background_color='lightyellow')],
    [sg.Text('请输入密码：')],
    [sg.Input(password_char='*', key='-PASSWORD-', size=(40, 1), background_color='lightblue')],
    [sg.Button('登录'), sg.Button('取消')]
]

# 创建窗口
window = sg.Window('登录界面', layout, size=(300, 220))

# 事件循环
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '取消':
        break
    if event == '登录':
        username = values['-USERNAME-']
        password = values['-PASSWORD-']
        sg.popup(f'用户名：{username}\n密码：{password}')

# 关闭窗口
window.close()