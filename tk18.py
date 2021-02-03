import tkinter as tk
def print_txtval():
    val_en = en.get()
    print(val_en)
    en.delete(0,tk.END)
root = tk.Tk()
en = tk.Entry()
en.insert(0,'entry any thing')
bt=tk.Button(text="ボタン", command = print_txtval)
[widget.pack() for widget in (en, bt)]
en.focus_set()
root.mainloop()