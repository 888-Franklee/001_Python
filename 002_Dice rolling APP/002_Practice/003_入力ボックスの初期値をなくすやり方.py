import PySimpleGUI as sg

# 定义一个带有默认提示文本的输入框
layout = [
    [sg.Input("输入数字", key="input1", enable_events=True, size=(60, 5), text_color='grey')],
    [sg.Button('提交'), sg.Button('取消')]
]

# 创建窗口
window = sg.Window('输入框提示文本示例', layout, size=(400,200))

# 默认提示文本
input1_default = "输入数字"
input1_empty = True  # 用于标记输入框是否为空

# 事件循环
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '取消':
        break

    # 当输入框获得焦点时，清除默认提示文本
    if event == 'input1':
        if input1_empty:
            window['input1'].update(value='', text_color='black')
            input1_empty = False
    
    # 当输入框失去焦点时，如果输入框为空，恢复默认提示文本
    if event != 'input1':
        if values['input1'] == '':
            window['input1'].update(value=input1_default, text_color='grey')
            input1_empty = True

    # 提交按钮事件：检查输入框内容是否有效
    if event == '提交':
        input_value = values['input1']
        if input_value == input1_default or input_value == '':
            sg.popup('请输入有效的数字')
        else:
            sg.popup(f'你输入的数字是：{input_value}')

# 关闭窗口
window.close()