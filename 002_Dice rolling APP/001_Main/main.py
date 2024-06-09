import PySimpleGUI as sg
import random

title="1~最大値のサイコロを振るアプリ"

label1,value1="数字を入力してください","初1期値 "

def dice(value1):
    max=int(value1)
    r=random.randint(1,max)
    return str(r)

def excute():
    value1=values["input1"]
    msg=dice(value1)
    window["text1"].update(msg)
    
layout=[[sg.Text(label1,size=(18,1)),sg.Input(label1,key="input1",size=(42,1))],
        [sg.Button("実行",size=(8,1),pad=(10,15),bind_return_key=True)],
        [sg.Multiline(key="text1",size=(60,10))]]
        
window=sg.Window(title,layout,font=(None,14))

while True:
   event,values=window.read()
   if event==None:
      break
   if event=="実行":
      excute()
      
window.close()