import tkinter as tk


def button_cb1():
    print("button 1 click")


def button_cb2(event):
    print("button 2 click")
    print("event.time=", event.time)
    print("event.type=", event.type)
    print("event.widgetId=", event.widget)
    print("event.keySymbol=", event.keysym)


def button_cb3():
    print("button 3 click")


wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello,Tkinter")

b1 = tk.Button(wm,
               text="button1",
               command=button_cb1,
               width=30,
               height=2
               )
b2 = tk.Button(wm,
               text="button2"
               )
b2.bind("<Return>", button_cb2)
b2["width"] = 30
b2["height"] = 3
b3 = tk.Button(wm,
               text="button3",
               command=button_cb3
               )
b3.configure(width=30, height=4)
b1.pack()
b2.pack()
b3.pack()
b2.focus_set()
wm.mainloop()

