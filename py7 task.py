#section e
import tkinter as tk

def submit():
    label.config(text="Hello " + entry.get())

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

label = tk.Label(root)
label.pack()

root.mainloop()