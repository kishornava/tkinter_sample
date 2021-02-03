import tkinter as tk
def print_txtval():
    sd_id = en1.get()
    sd_name = en2.get()
    print('Student id =',sd_id)
    print('Student name=',sd_name)
    en1.delete(0,tk.END)
    en2.delete(0,tk.END)

root = tk.Tk()
root.geometry("150x150+500+500")
lb1 = tk.Label(text = 'Student ID')
en1 = tk.Entry()
lb2 = tk.Label(text = 'Name')
en2 = tk.Entry()
bt=tk.Button(text="INSERT", command = print_txtval)
[widget.pack() for widget in (lb1,en1,lb2,en2,bt)]
root.mainloop()
