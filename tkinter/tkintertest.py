# gui人机界面


import tkinter as tk
window = tk.Tk()

window.title('Tkinter测试')

window.geometry('800x400')

# entry = tk.Entry(window)
# entry.pack()

button = tk.Button(window, text='resume')
button.pack()

label = tk.Label(window, text='hello world')
label.pack()

window.mainloop()
