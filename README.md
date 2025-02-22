# Task Manager

A simple task management application built with Python and Tkinter that allows users to create, manage, and track tasks efficiently.

## Features

- **Add Tasks**: Easily create new tasks with a title, description, priority, due date, and category.
- **Edit Tasks**: Update existing tasks with new information.
- **Delete Tasks**: Remove tasks from your list.
- **Mark Tasks as Completed**: Track completed tasks for better organization.
- **Persistent Storage**: Tasks are saved to a CSV file for persistence across sessions.

#  Implementation Overview
The provided code snippet implements the Task Manager's core functionalities using Tkinter. Here are some key components:

#Task Management Functions:

load_tasks: Loads existing tasks from the CSV file into a list.

save_tasks: Saves the current list of tasks back to the CSV file.

validate_input: Ensures that user inputs are not empty.

add_task, edit_task, delete_task, and mark_complete: Functions to manage task operations.

User Interface: The GUI is created using Tkinter, featuring a main window with a title, a listbox for displaying tasks, and buttons for performing task operations.

Event Handling: Each button is linked to its corresponding function, ensuring that user interactions trigger the appropriate functionality.

Data Persistence:The application maintains task data between sessions by loading from and saving to a CSV file.

#Conclusion
The Task Manager application demonstrates a solid implementation of task management functionality using Tkinter. By focusing on usability and data persistence, the application serves as an effective tool for users to enhance their productivity and organization. 

## Installation

Clone the Repository:

```bash
<<<<<<< HEAD
git clone https://github.com/Barsha100/Task--manager.git
=======
https://github.com/Barsha100/Tkinter-Task-Manager.git
>>>>>>> bb6c2154635047e16d87cf218cd91c647b31ee68
