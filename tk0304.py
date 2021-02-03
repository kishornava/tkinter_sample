# -*- coding: utf-8 -*-
#tk0304.pyw
#This will positions the box

import tkinter as tk
root = tk.Tk()
root.title('NAVA')
#root.geometry('600*400')
root.eval('tk::PlaceWindow . center')
root.mainloop()