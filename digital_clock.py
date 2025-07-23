# CodSoft Python Programming Internship
# Task 3: Digital Clock (GUI Version)
# Developed by: [Your Name]
# Date: [Submission Date]

import tkinter as tk
from time import strftime

# Update time on the label
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# GUI Setup
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.config(bg="#1e1e1e")

label = tk.Label(root, font=('ds-digital', 60), background='#1e1e1e', foreground='#00FF00')
label.pack(expand=True)

time()
root.mainloop()
