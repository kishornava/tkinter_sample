#-*- coding: utf-8 -*-
#tk25.pyw

import tkinter as tk
def get_text():
    print(txt.get("1.5","3.4"))
root = tk.Tk()
txt = tk.Text(width=30,height=5)
bt = tk.Button(text='1 line 6 letter from 3 line 4 letter ', command = get_text)
[widget.pack()for widget in (txt,bt)]
root.mainloop()
