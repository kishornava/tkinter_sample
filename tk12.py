#-*- coding: utf-8 -*-
#tk12.pyw
import tkinter as tk
root = tk.Tk()
root.geometry("200x150")
lb_rgb = tk.Label(text="rgb",fg="#000",bg="#fff")
lb_rrggbb= tk.Label(text = "rrggbb", fg="#abcdef", bg="#123456")
lb_rrrgggbbb = tk.Label(text="rrrgggbbb", fg="#123456789", bg="#987abcdef")
lb_colorname = tk.Label(text = "colorname",fg ="magenta", bg="yellow")
[widget.pack() for widget in (lb_rgb, lb_rrggbb, lb_rrrgggbbb, lb_colorname)]
root.mainloop()
