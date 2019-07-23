import tkinter as tk

wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello, Tkinter")

v1 = tk.IntVar()
v2 = tk.IntVar()
v1.set(0)
v2.set(1)
for v in [v1, v2]:
    for i in range(3):
        tk.Radiobutton(wm,
                       variable=v,
                       text="python"+str(i),
                       value=i
                       ).pack()

# tk.Radiobutton(wm,
#                text="python"
#                ).pack()
# tk.Radiobutton(wm,
#                text="tkinter"
#                ).pack()
# tk.Radiobutton(wm,
#                text="widget"
#                ).pack()
wm.mainloop()
