# Modern Web-Style Calculator using Python Tkinter
# FIXED: Auto replace operators (+ - * / %)

import tkinter as tk

# ---------------- Window Setup ----------------
root = tk.Tk()
root.title("Web Style Python Calculator")
root.geometry("360x520")
root.configure(bg="#121212")
root.resizable(False, False)

# ---------------- Variables ----------------
expression = ""
operators = "+-*/%"

# ---------------- Functions ----------------
def press(value):
    global expression

    # If operator is pressed
    if value in operators:
        if not expression:
            return  # no operator at start
        if expression[-1] in operators:
            expression = expression[:-1]  # replace last operator

    expression += value
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def erase():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression

    if not expression:
        return

    while expression[-1] in operators:
        expression = expression[:-1]

    try:
        result = eval(expression)
        expression = str(result)
        display_var.set(expression)
    except:
        display_var.set("Error")
        expression = ""

# ---------------- Display ----------------
display_var = tk.StringVar()
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 26),
    bg="#1e1e1e",
    fg="white",
    bd=0,
    justify="right"
)
display.pack(fill="x", padx=20, pady=20, ipady=15)

# ---------------- Buttons Frame ----------------
frame = tk.Frame(root, bg="#121212")
frame.pack(padx=10)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

# ---------------- Button Creator ----------------
def create_btn(text, row, col, color="#2d2d2d", cmd=None):
    tk.Button(
        frame,
        text=text,
        font=("Segoe UI", 15),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#3d3d3d",
        activeforeground="white",
        width=6,
        height=1,
        command=cmd if cmd else lambda: press(text)
    ).grid(row=row, column=col, padx=6, pady=6, sticky="nsew")

# ---------------- Buttons ----------------
create_btn("C", 0, 0, "#ff5c5c", clear)
create_btn("⌫", 0, 1, "#ff8c42", erase)
create_btn("%", 0, 2)
create_btn("/", 0, 3, "#6c63ff")

create_btn("7", 1, 0)
create_btn("8", 1, 1)
create_btn("9", 1, 2)
create_btn("*", 1, 3, "#6c63ff")

create_btn("4", 2, 0)
create_btn("5", 2, 1)
create_btn("6", 2, 2)
create_btn("-", 2, 3, "#6c63ff")

create_btn("1", 3, 0)
create_btn("2", 3, 1)
create_btn("3", 3, 2)
create_btn("+", 3, 3, "#6c63ff")

create_btn("0", 4, 0)
create_btn(".", 4, 1)

# ---------------- Equal Button ----------------
tk.Button(
    frame,
    text="=",
    font=("Segoe UI", 15),
    bg="#4CAF50",
    fg="white",
    bd=0,
    activebackground="#5fd067",
    activeforeground="white",
    height=1,
    command=calculate
).grid(row=4, column=2, columnspan=2, padx=6, pady=6, sticky="nsew")

# ---------------- Run App ----------------
root.mainloop()
