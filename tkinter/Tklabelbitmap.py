import tkinter as tk

wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello, Tkinter")
tk.Label(wm,
         text="error",
         bg="red",
         compound="center",
         bitmap="error",
         ).pack()
tk.Label(wm,
         text="blue",
         bg="blue",
         width="10",
         height="3"
         ).pack()
tk.Label(wm,
         text="welcome to Tkinter world",
         bg="yellow",
         width="10",
         height="3",
         wraplength="80",
         justify="right"
         ).pack()
wm.mainloop()


# wm = tk.Tk()
# wm.geometry("800x400")
# wm.title("Hello, Tkinter")
# label = tk.Label(wm, bitmap="info")
# tk.Label(wm,
#          fg="black",
#          bg="yellow",
#          text="Hello Tkinter"
#          ).pack()
# wm.mainloop()

