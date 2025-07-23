# CodSoft Python Programming Internship
# Task 2: To-Do List App (GUI Version)
# Developed by: [Your Name]
# Date: [Submission Date]

import tkinter as tk
from tkinter import messagebox

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        open("tasks.txt", "w").close()

# Save tasks to file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Delete selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
        save_tasks()
    else:
        messagebox.showwarning("Select Task", "No task selected.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.config(bg="#e8f0fe")

tk.Label(root, text="Enter a Task:", bg="#e8f0fe", font=("Arial", 12)).pack(pady=10)
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

tk.Button(root, text="Add Task", width=20, bg="#4CAF50", fg="white", command=add_task).pack(pady=5)
tk.Button(root, text="Delete Selected", width=20, bg="#f44336", fg="white", command=delete_task).pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=40)
task_listbox.pack(pady=10)

# Load existing tasks
load_tasks()

root.mainloop()                