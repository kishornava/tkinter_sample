#-*- coding: utf-8 -*-
#tk14.pyw
import tkinter as tk
root = tk.Tk()
root.geometry("250x250")
ms_dict ={}
for relief_val in["flat","raised","sunken","groove","ridge"]:
#枠の種類は使う、ここではループで種類を回し設定
    ms_dict[relief_val]= tk.Message(text=relief_val, relief=relief_val ,bd=10)
    ms_dict[relief_val].pack()
root.mainloop()