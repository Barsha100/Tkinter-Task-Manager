<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# File to store tasks
TASKS_FILE = "tasks.csv"

# Load tasks from CSV file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            tasks = list(reader)
    return tasks

# Save tasks to CSV file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Function to add a new task
def add_task():
    task_title = simpledialog.askstring("Add Task", "Enter Task Title:")
    if not task_title:
        messagebox.showerror("Error", "Task title cannot be empty.")
        return
    
    task_description = simpledialog.askstring("Task Description", "Enter Task Description:")
    task_priority = simpledialog.askstring("Priority", "Enter Priority (High/Medium/Low):")
    task_due_date = simpledialog.askstring("Due Date", "Enter Due Date (YYYY-MM-DD):")
    task_category = simpledialog.askstring("Category", "Enter Task Category:")

    tasks.append([task_title, task_description, task_priority, task_due_date, task_category, "Incomplete"])
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task added successfully!")

# Function to edit a selected task
def edit_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to edit.")
        return

    index = selected_index[0]
    new_title = simpledialog.askstring("Edit Task", "Enter new Task Title:", initialvalue=tasks[index][0])
    if not new_title:
        return
    
    new_description = simpledialog.askstring("Task Description", "Enter new Task Description:", initialvalue=tasks[index][1])
    new_priority = simpledialog.askstring("Priority", "Enter new Priority (High/Medium/Low):", initialvalue=tasks[index][2])
    new_due_date = simpledialog.askstring("Due Date", "Enter new Due Date (YYYY-MM-DD):", initialvalue=tasks[index][3])
    new_category = simpledialog.askstring("Category", "Enter new Task Category:", initialvalue=tasks[index][4])

    tasks[index] = [new_title, new_description, new_priority, new_due_date, new_category, tasks[index][5]]
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task updated successfully!")

# Function to delete a selected task
def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to delete.")
        return

    index = selected_index[0]
    del tasks[index]
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task deleted successfully!")

# Function to mark task as completed
def mark_complete():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to mark as completed.")
        return

    index = selected_index[0]
    tasks[index][5] = "Completed"
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task marked as completed!")

# Function to update the task list in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task[5] == "Completed" else "❌"
        task_listbox.insert(tk.END, f"{task[0]} - {task[3]} [{status}]")

# Function to exit the application
def exit_app():
    root.destroy()

# Main Tkinter window
root = tk.Tk()
root.title("Task Manager")
root.geometry("500x400")

# Load existing tasks
tasks = load_tasks()

# Title label
title_label = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Task list
task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12)
edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, width=12)
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12)
complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete, width=12)
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=12)

add_button.grid(row=0, column=0, padx=5, pady=5)
edit_button.grid(row=0, column=1, padx=5, pady=5)
delete_button.grid(row=0, column=2, padx=5, pady=5)
complete_button.grid(row=0, column=3, padx=5, pady=5)
exit_button.grid(row=1, column=1, columnspan=2, pady=10)

# Populate initial task list
update_task_list()

# Run the application
root.mainloop() 
=======
import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# File to store tasks
TASKS_FILE = "tasks.csv"

# Load tasks from CSV file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            tasks = list(reader)
    return tasks

# Save tasks to CSV file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Function to add a new task
def add_task():
    task_title = simpledialog.askstring("Add Task", "Enter Task Title:")
    if not task_title:
        messagebox.showerror("Error", "Task title cannot be empty.")
        return
    
    task_description = simpledialog.askstring("Task Description", "Enter Task Description:")
    task_priority = simpledialog.askstring("Priority", "Enter Priority (High/Medium/Low):")
    task_due_date = simpledialog.askstring("Due Date", "Enter Due Date (YYYY-MM-DD):")
    task_category = simpledialog.askstring("Category", "Enter Task Category:")

    tasks.append([task_title, task_description, task_priority, task_due_date, task_category, "Incomplete"])
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task added successfully!")

# Function to edit a selected task
def edit_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to edit.")
        return

    index = selected_index[0]
    new_title = simpledialog.askstring("Edit Task", "Enter new Task Title:", initialvalue=tasks[index][0])
    if not new_title:
        return
    
    new_description = simpledialog.askstring("Task Description", "Enter new Task Description:", initialvalue=tasks[index][1])
    new_priority = simpledialog.askstring("Priority", "Enter new Priority (High/Medium/Low):", initialvalue=tasks[index][2])
    new_due_date = simpledialog.askstring("Due Date", "Enter new Due Date (YYYY-MM-DD):", initialvalue=tasks[index][3])
    new_category = simpledialog.askstring("Category", "Enter new Task Category:", initialvalue=tasks[index][4])

    tasks[index] = [new_title, new_description, new_priority, new_due_date, new_category, tasks[index][5]]
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task updated successfully!")

# Function to delete a selected task
def delete_task():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to delete.")
        return

    index = selected_index[0]
    del tasks[index]
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task deleted successfully!")

# Function to mark task as completed
def mark_complete():
    selected_index = task_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Error", "Please select a task to mark as completed.")
        return

    index = selected_index[0]
    tasks[index][5] = "Completed"
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task marked as completed!")

# Function to update the task list in the GUI
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task[5] == "Completed" else "❌"
        task_listbox.insert(tk.END, f"{task[0]} - {task[3]} [{status}]")

# Function to exit the application
def exit_app():
    root.destroy()

# Main Tkinter window
root = tk.Tk()
root.title("Task Manager")
root.geometry("500x400")

# Load existing tasks
tasks = load_tasks()

# Title label
title_label = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Task list
task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12)
edit_button = tk.Button(button_frame, text="Edit Task", command=edit_task, width=12)
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12)
complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete, width=12)
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=12)

add_button.grid(row=0, column=0, padx=5, pady=5)
edit_button.grid(row=0, column=1, padx=5, pady=5)
delete_button.grid(row=0, column=2, padx=5, pady=5)
complete_button.grid(row=0, column=3, padx=5, pady=5)
exit_button.grid(row=1, column=1, columnspan=2, pady=10)

# Populate initial task list
update_task_list()

# Run the application
root.mainloop() 
>>>>>>> bb6c2154635047e16d87cf218cd91c647b31ee68
