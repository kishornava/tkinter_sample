#-*- coding: utf-8 -*-
#tk17.pyw
import tkinter as tk
root = tk.Tk()
bt_dict = {}
for bitmap_val in ['info','error','gray12','gray25','gray50','gray75','hourglass','questhead','question','warning']:
    bt_dict[bitmap_val] = tk.Button(bitmap=bitmap_val)
    bt_dict[bitmap_val].pack()
root.mainloop()