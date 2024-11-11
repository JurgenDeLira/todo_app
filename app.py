import tkinter as tk
from tkinter import messagebox
from task_manager import add_task, delete_task, complete_task
from utils import update_task_listbox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")  # Tamaño de la ventana

        # Lista de tareas
        self.tasks = []

        # Creación de los widgets
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.grid(row=0, column=0, padx=20, pady=10)

        self.task_entry = tk.Entry(self.root, width=52)
        self.task_entry.grid(row=1, column=0, padx=20, pady=10)

        self.add_button = tk.Button(self.root, text="Añadir Tarea", width=20, command=self.add_task)
        self.add_button.grid(row=2, column=0, pady=10)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", width=20, command=self.delete_task)
        self.delete_button.grid(row=3, column=0, pady=10)

        self.complete_button = tk.Button(self.root, text="Marcar Completada", width=20, command=self.complete_task)
        self.complete_button.grid(row=4, column=0, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if add_task(task, self.tasks):
            update_task_listbox(self.task_listbox, self.tasks)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            if delete_task(selected_task_index, self.tasks):
                update_task_listbox(self.task_listbox, self.tasks)
            else:
                messagebox.showwarning("Selección inválida", "Por favor seleccione una tarea para eliminar.")
        except IndexError:
            messagebox.showwarning("Selección inválida", "Por favor seleccione una tarea para eliminar.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            if complete_task(selected_task_index, self.tasks):
                update_task_listbox(self.task_listbox, self.tasks)
            else:
                messagebox.showwarning("Selección inválida", "Por favor seleccione una tarea para marcar como completada.")
        except IndexError:
            messagebox.showwarning("Selección inválida", "Por favor seleccione una tarea para marcar como completada.")

# Crear la ventana principal
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
