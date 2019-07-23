import tkinter as tk


def radiobuttonCb1():
    print("radiobutton cb1")


def radiobuttonCb2():
    print("radiobutton cb2")


def radiobuttonCb3():
    print("radiobutton cb3")


def radiobuttonCb4():
    print("radiobutton cb4")


wm = tk.Tk()
wm.geometry("800x400")
wm.title("hello, Tkinter")
v = tk.IntVar()
v.set(0)
i = 0
for rcb in [radiobuttonCb1, radiobuttonCb2, radiobuttonCb3, radiobuttonCb4]:
    tk.Radiobutton(wm,
                   variable=v,
                   text="radiobutton"+str(i),
                   value=i,
                   command=rcb
                   ).pack()
    i = i+1
wm.mainloop()

