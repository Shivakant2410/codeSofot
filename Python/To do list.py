import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
from tkinter import ttk

task = []
def add_task():
   task = task_entry.get()
   if task != "":
      tasks_listbox.insert(tk.END, task)
      task_entry.delete(0, tk.END)
   else:
      messagebox.showwarning("Warning","You must enter a task")  
def delete_task():
    try:
       selected_task_index = tasks_listbox.curselection()[0]
       tasks_listbox.delete(selected_task_index)
    except:
       messagebox.showwarning("Warning","You must select a task to delete")

root = tk.Tk()
root.title("To-DO List")             

frame = tk.Frame(root)
frame.pack(padx=10)

# Create a listbox
tasks_listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    font=("Helvetica", 12),
    selectbackground="#a6a6a6"
)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Attach the scrollbar to the listbox
tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

# Create an entry widget
task_entry = tk.Entry(
    root,
    font=("Helvetica", 12)
)
task_entry.pack(pady=20)

# Create a button to add tasks
add_task_button = tk.Button(
    root,
    text="Add Task",
    command=add_task
)
add_task_button.pack(pady=10)

# Create a button to delete tasks
delete_task_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task
)
delete_task_button.pack(pady=10)

# Run the main event loop
root.mainloop()
