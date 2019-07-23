import tkinter as tk

wm = tk.Tk()
wm.geometry("800x400")
wm.title("hello, Tkinter")

lb = tk.Listbox(wm,
                selectmode="extended")
for item in ["python", "tkinter", "widget"]:
    lb.insert("end", item)
lb.insert("end", "linux", "windows", "unix")
lb.pack()
wm.mainloop()
