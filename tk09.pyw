#-*- coding: utf-8 -*-
#tk09.pyw

import tkinter as tk
root = tk.Tk()
root.title(".config()")
root.geometry("350x150")
lb = tk.Label()
print(lb.config())
root.mainloop()