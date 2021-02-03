#-*- coding: utf-8 -*-
#tk27.pyw
import tkinter as tk
def ins_cursor_point():
    txt.insert(txt.index("insert"),"+++++")
root = tk.Tk()
txt = tk.Text(width=30,height=5)
bt=tk.Button(text='click', command = get_text)
[widget.pack() for widget in (txt ,bt)]
root.mainloop()