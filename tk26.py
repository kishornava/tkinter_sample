#-*- coding: utf-8 -*-
#tk26.pyw
import tkinter as tk
def print_selpoint():
    sel_start = txt.index("sel.first")
    sel_end = txt.index('sel.last')
    print(txt.get(sel_start , sel_end))
root = tk.Tk()
txt = tk.Text(width=30, height=5)
bt = tk.Button(text='SAVE', command = print_selpoint)
[widget.pack() for widget in (txt,bt)]
root.mainloop()