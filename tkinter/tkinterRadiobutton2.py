import tkinter as tk

wm = tk.Tk()
wm.geometry("800x400")
wm.title("hello, Tkinte")

v = tk.IntVar()
v.set(0)
for i in range(3):
    tk.Radiobutton(wm,
                   variable=v,
                   value=1,
                   text="python"+str(i)
                   ).pack()
for i in range(3):
    tk.Radiobutton(wm,
                   variable=v,
                   value=i,
                   text="python"+str(2+i)
                   ).pack()
wm.mainloop()
