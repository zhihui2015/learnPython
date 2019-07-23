import tkinter as tk

wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello, Tkinter")

e = tk.StringVar()
entry = tk.Entry(wm,
         textvariable=e
         )
e.set("input your text here")
entry.pack()
entry['show'] = '*'
# for mask in ['*', '#', '$']:
#     e = tk.StringVar()
#     entry = tk.Entry(wm,
#                      textvariable=e
#                      )
#     e.set('password')
#     entry.pack()
#     entry['show'] = mask
wm.mainloop()
