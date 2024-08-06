import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a selected task as completed
def mark_task_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} - Completed")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Setting up the main window
root = tk.Tk()
root.title("To-Do List App")

# Creating the task entry widget
task_entry = tk.Entry(root, width=50, borderwidth=5)
task_entry.pack(pady=10)

# Creating the add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Creating the listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10, borderwidth=5)
tasks_listbox.pack(pady=10)

# Creating the delete task button
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Creating the mark task completed button
mark_task_completed_button = tk.Button(root, text="Mark Task Completed", command=mark_task_completed)
mark_task_completed_button.pack(pady=5)

# Running the main loop
root.mainloop()
