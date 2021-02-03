#-*- coding: utf-8 -*-
#tk16.pyw
import tkinter as tk
def btn_press():
    print("ボタンが押されました")
root = tk.Tk()
root.geometry("150x80")
bt=tk.Button(text="ボタン",command = btn_press)
bt.pack()
root.mainloop()