import tkinter as tk


# def buttoncb():
#     print("button click")


# def statePrint():
#     print('state')

def changeText():
    if b['text'] == 'text':
        v.set('change')
        print('change')
    else:
        v.set('text')
        print('text')



wm = tk.Tk()
wm.geometry("800x400")
wm.title("Hello, Tkinter")


v = tk.StringVar()
b = tk.Button(wm,
              textvariable=v,
              command=changeText
              )
v.set('start')
b.pack()

# for r in ['normal', 'active', 'disable']:
#     tk.Button(wm,
#               text=r,
#               state=r,
#               width=30,
#               command=statePrint
#               ).pack()

# for r in ['raised', 'sunken', 'groove', 'ridge']:
#     tk.Button(wm,
#               text=r,
#               relief=r,
#               width=30,
#               command=buttoncb
#               ).pack()

# i = 0
# for a in ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw']:
#     i = i+1
#     tk.Button(wm,
#               text=str(i),
#               anchor=a,
#               width=10,
#               height=4,
#               fg="red",
#               bg="yellow",
#               bd=i
#               ).pack()
wm.mainloop()
