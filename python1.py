from tkinter import *
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected = task_listbox.curselection()
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task!")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, END)

# Main Window
root = Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry Box
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add Button
add_btn = Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Listbox
task_listbox = Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Delete Button
delete_btn = Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Clear Button
clear_btn = Button(root, text="Clear All Tasks", command=clear_tasks)
clear_btn.pack(pady=5)

root.mainloop()
