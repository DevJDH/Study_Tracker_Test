import tkinter as tk

root = tk.Tk()
root.geometry("550x350")
root.title('simple app')

frame = tk.Frame(root)
frame.grid(row = 0, column = 0)

def click():
     lbl.config(text="nigga")

btn = tk.Button(frame, text = "button 1",command= click)
btn.grid(row=0, column=1)

lbl = tk.Label(frame, text='label 1')
lbl.grid(row=0, column = 3)

















root.mainloop()