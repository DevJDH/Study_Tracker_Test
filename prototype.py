import tkinter as tk

root = tk.Tk()
# importing the library

root.title('simple app')
root.geometry("500x500")

# def click():
#     lbl.config(text = "nigga")

# btn = tk.Button(root, text="button 1",command = click)
# lbl = tk.Label(root, text = "label 1")

# lbl.grid(row = 0, column = 0)
# btn.grid(row = 0, column = 1)

# some work with functionality of buttons and other

def add_to_list(event):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)



frame = tk.Frame(root)
frame.grid(row = 0, column=0)

entry = tk.Entry(frame)
entry.grid(row = 0, column=0)

entry.bind("<Return>", add_to_list)

entry_btn = tk.Button(frame, text="add", command= add_to_list)
entry_btn.grid(row=1,column=1)

text_list = tk.Listbox(frame)
text_list.grid(row = 1,column = 0)


























root.mainloop()