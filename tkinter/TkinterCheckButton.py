import tkinter as tk


def checkButtonCb():
    print(v.get())


wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello, Tkinter")
v = tk.StringVar()
tk.Checkbutton(wm,
               text='checkbutton value',
               variable=v,
               command=checkButtonCb,
               onvalue='python',
               offvalue='tkinter'
               ).pack()
wm.mainloop()
