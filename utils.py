import tkinter as tk

def update_task_listbox(task_listbox, tasks):
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
