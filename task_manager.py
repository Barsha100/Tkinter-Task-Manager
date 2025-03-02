import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, PhotoImage, Label
import csv
import os
from datetime import datetime

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

# Function to validate input
def validate_input(value, field_name):
    if not value:
        messagebox.showerror("Input Error", f"{field_name} cannot be empty.")
        return False
    return True
# Function to validate date format
def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        messagebox.showerror("Input Error", "Invalid Date Format! Use YYYY-MM-DD.")
        return False

# Function to add a new task
def add_task():
    task_title = simpledialog.askstring("Add Task", "Enter Task Title:")
    if not validate_input(task_title, "Task Title"):
        return

    task_description = simpledialog.askstring("Task Description", "Enter Task Description:")
    task_priority = simpledialog.askstring("Priority", "Enter Priority (High/Medium/Low):")
    task_due_date = simpledialog.askstring("Due Date", "Enter Due Date (YYYY-MM-DD):")
    # Validate Date Format
    if not validate_date_format(task_due_date):
        return
    task_category = simpledialog.askstring("Category", "Enter Task Category:")

    tasks.append([task_title, task_description, task_priority, task_due_date, task_category, "Incomplete"])
    save_tasks(tasks)
    update_task_list()
    messagebox.showinfo("Success", "Task added successfully!")
    status_label.config(text="Status: Task added successfully!", fg="green")

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
    status_label.config(text="Status: Task deleted successfully!", fg="red")

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

# Function to open the task details window
def open_task_window():
    task_window = Toplevel(root)
    task_window.title("Task Details")
    task_window.geometry("400x300")

    task_label = Label(task_window, text="Task Details", font=("Arial", 14, "bold"))
    task_label.pack(pady=10)

    task_list = tk.Listbox(task_window, width=50, height=10)
    task_list.pack(pady=10)

    for task in tasks:
        status = "✅" if task[5] == "Completed" else "❌"
        task_list.insert(tk.END, f"{task[0]} - {task[3]} [{status}]")

    close_button = tk.Button(task_window, text="Close", command=task_window.destroy)
    close_button.pack(pady=10)

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
root.geometry("500x540")

# Load existing tasks
tasks = load_tasks()

# Title label
title_label = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Manage your tasks efficiently. Use the buttons below.", font=("Arial", 12))
instruction_label.pack(pady=5)

# Status label (will update dynamically)
status_label = tk.Label(root, text="Status: Ready", font=("Arial", 10), fg="blue")
status_label.pack(pady=5)

# Task list
task_listbox = tk.Listbox(root, width=60, height=10)
task_listbox.pack(pady=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Load and resize images
add_icon = tk.PhotoImage(file="add_icon.png").subsample(5, 5)
edit_icon = tk.PhotoImage(file="edit_icon.png").subsample(5, 5)

# Buttons
add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=180, bg="green", fg="white", image=add_icon, compound="left")
view_button = tk.Button(button_frame, text="View Tasks", command=open_task_window, width=180, bg="blue", fg="white", image=edit_icon, compound="left")
delete_button = tk.Button(button_frame, text="Delete", command=delete_task, width=20, bg="red", fg="white")
mark_complete_button = tk.Button(button_frame, text="Mark Complete", command=mark_complete, width=20, bg="yellow", fg="black")
exit_button = tk.Button(button_frame, text="Exit", command=exit_app, width=20, bg="gray", fg="white")

add_button.grid(row=0, column=0, padx=5, pady=5)
view_button.grid(row=0, column=1, padx=5, pady=5)
delete_button.grid(row=1, column=0, padx=5, pady=5)
mark_complete_button.grid(row=1, column=1, padx=5, pady=5)
exit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Populate initial task list
update_task_list()

# Run the application
root.mainloop()
