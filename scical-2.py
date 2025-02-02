import tkinter as tk
import math

# Global variables
memory_value = None
use_degrees = True  # Default mode is degrees

# Function to handle button click
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())  # Eval is safe since user cannot type directly
            screen.set(result)
        except Exception:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

# Function to handle advanced operations
def advanced_function(func):
    try:
        value = float(screen.get())
        if use_degrees and func in {"sin", "cos", "tan"}:
            value = math.radians(value)
        result = getattr(math, func)(value)  # Calls math.sin, math.cos, etc.
        screen.set(result)
    except Exception:
        screen.set("Error")

# Function to store and recall memory
def store_memory():
    global memory_value
    try:
        memory_value = eval(screen.get())  # Still safe since input is restricted
        screen.set(f"Stored: {memory_value}")
    except Exception:
        screen.set("Error")

def recall_memory():
    global memory_value
    if memory_value is not None:
        screen.set(memory_value)
    else:
        screen.set("No Value Stored")

# Toggle between degrees and radians
def toggle_mode():
    global use_degrees
    use_degrees = not use_degrees
    mode_label.config(text="Mode: Degrees" if use_degrees else "Mode: Radians")

# Initialize tkinter GUI
root = tk.Tk()
root.title("SCI-CA")
root.geometry("500x850")

# Input screen (readonly)
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bd=10, relief=tk.SUNKEN, justify="right", state="readonly")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Mode label
mode_label = tk.Label(root, text="Mode: Degrees", font="lucida 12 bold")
mode_label.pack(pady=5)

# Toggle button for mode
toggle_button = tk.Button(root, text="Toggle Degrees/Radians", font="lucida 12", command=toggle_mode)
toggle_button.pack(pady=5)

# Create button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ["1", "2", "3", "/"],
    ["4", "5", "6", "*"],
    ["7", "8", "9", "-"],
    ["C", "0", ".", "+"],
    ["sin", "cos", "tan", "="],
    ["log", "ln", "sqrt", "**"],
    ["(", ")", "π", "e"],
    ["M", "MR"]  # Memory buttons
]

# Add buttons to the GUI
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text in {"sin", "cos", "tan", "log", "ln", "sqrt"}:
            btn = tk.Button(
                button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                command=lambda func=btn_text: advanced_function(func)
            )
        elif btn_text == "M":  # Memory store button
            btn = tk.Button(
                button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                command=store_memory
            )
        elif btn_text == "MR":  # Memory recall button
            btn = tk.Button(
                button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                command=recall_memory
            )
        elif btn_text in {"π", "e"}:
            btn = tk.Button(
                button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                command=lambda const=btn_text: screen.set(screen.get() + str(math.pi if const == "π" else math.e))
            )
        else:
            btn = tk.Button(
                button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15
            )
            btn.bind("<Button-1>", click)
        btn.grid(row=i, column=j, padx=5, pady=5)

# Initialize the calculator
screen.set("")
root.mainloop()
