import tkinter as tk


def happybutton():
    print("hello button")
    tk.Label(wm,
             text="Hello,button",
             bg="yellow"
             ).pack()


wm = tk.Tk()
wm.title("button")
wm.geometry("800x400")
tk.Button(wm,
          text="Hello Button",
          command=happybutton,
          relief="groove",
          compound="left",
          bitmap="error"
          ).pack()
wm.mainloop()
