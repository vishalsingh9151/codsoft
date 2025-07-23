# calculator_gui.py

import tkinter as tk
from tkinter import messagebox

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1 * num2
        elif op == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result:")

# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x300")
root.config(bg="#f9f9f9")

tk.Label(root, text="Enter First Number:", bg="#f9f9f9").grid(row=0, column=0, pady=10, padx=10, sticky="w")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10)

tk.Label(root, text="Enter Second Number:", bg="#f9f9f9").grid(row=1, column=0, pady=10, padx=10, sticky="w")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10)

tk.Label(root, text="Choose Operation:", bg="#f9f9f9").grid(row=2, column=0, pady=10, padx=10, sticky="w")

# Operation Buttons
tk.Button(root, text="Add", bg="#4CAF50", fg="white", width=10, command=lambda: calculate("Add")).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Subtract", bg="#2196F3", fg="white", width=10, command=lambda: calculate("Subtract")).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Multiply", bg="#FF9800", fg="white", width=10, command=lambda: calculate("Multiply")).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Divide", bg="#f44336", fg="white", width=10, command=lambda: calculate("Divide")).grid(row=4, column=1, padx=10, pady=5)

# Clear Button
tk.Button(root, text="Clear", bg="#9E9E9E", fg="white", width=22, command=clear_fields).grid(row=5, column=0, columnspan=2, pady=10)

# Result
result_label = tk.Label(root, text="Result:", bg="#f9f9f9", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()