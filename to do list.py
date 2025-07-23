import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("My To-Do List")
root.geometry("600x400")
root.config(bg="#f0f8ff")

conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tasks 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
conn.commit()

tasks = []

def refresh_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def add_new_task():
    new_task = entry.get()
    if new_task == "":
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        tasks.append(new_task)
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (new_task,))
        conn.commit()
        refresh_list()
        entry.delete(0, tk.END)

def remove_task():
    try:
        selected = task_list.get(task_list.curselection())
        tasks.remove(selected)
        cursor.execute("DELETE FROM tasks WHERE task=?", (selected,))
        conn.commit()
        refresh_list()
    except:
        messagebox.showwarning("Warning", "Please select a task to remove")

def clear_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        cursor.execute("DELETE FROM tasks")
        conn.commit()
        refresh_list()

def load_tasks():
    tasks.clear()
    for row in cursor.execute("SELECT task FROM tasks"):
        tasks.append(row[0])
    refresh_list()

label = tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f0f8ff")
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=10)

add_btn = tk.Button(button_frame, text="Add Task", width=12, command=add_new_task)
add_btn.grid(row=0, column=0, padx=5)

remove_btn = tk.Button(button_frame, text="Remove Task", width=12, command=remove_task)
remove_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(button_frame, text="Clear All", width=12, command=clear_all)
clear_btn.grid(row=0, column=2, padx=5)

task_list = tk.Listbox(root, width=50, height=12, font=("Arial", 12), bg="white")
task_list.pack(pady=10)

load_tasks()

root.mainloop()

cursor.close()
conn.close()
