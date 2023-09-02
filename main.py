import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import json

import sv_ttk



def add_task():
    task_list.insert(tk.END, entry.get())
    entry.delete(0,tk.END)

def delete_task():
    task_list.delete(tk.ANCHOR)


def finish_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, fg="#39FF14")
        task_list.selection_clear(selected_task)

def unfinish_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.itemconfig(selected_task, fg="#212121")
        task_list.selection_clear(selected_task)

def delete_completed_tasks():
    for i in reversed(range(task_list.size())):
        if task_list.itemcget(i, "fg") == "#39FF14":
            task_list.delete(i)


def save():
    tasks_data = []
    for i in range(task_list.size()):
        text = task_list.get(i)
        completed = task_list.itemcget(i, "fg") == "#39FF14"
        tasks_data.append({"text": text, "completed": completed})

    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file)


def load():
    if task_list.size() == 0:
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)

            for task_data in tasks_data:
                text = task_data["text"]
                completed = task_data["completed"]
                task_list.insert(tk.END, text)

                if completed:
                    task_index = task_list.size() - 1 
                    task_list.itemconfig(task_index, {'fg': '#39FF14'})
 
                    

        except FileNotFoundError:
            pass
    pass


    


def on_enter(event):
    if len(entry.get()) > 0:
        add_task()


window = tk.Tk()
window.title("Task Todo List")
window.geometry("650x600")

font = Font(
    family= "helvetica",
    size=30,
    weight="bold")


# create frame , listbox, scroll bar
frame = ttk.Frame(window)
frame.pack( pady=10, fill="both", expand=True)


label = ttk.Label(frame, text="TASKS FOR TODAY", font=font)
label.pack()

y_task_scrollbar = ttk.Scrollbar(frame)
y_task_scrollbar.pack(side="right", fill="both")

x_task_scrollbar = ttk.Scrollbar(frame, orient="horizontal")
x_task_scrollbar.pack(side="bottom", fill="x")

    

task_list = tk.Listbox(frame,  width=25, height=5,font=font, bg="SystemButtonFace", bd=0, fg="#212121", 
                       highlightthickness=0, selectbackground="#a1a1a1", activestyle="none",
                       yscrollcommand= y_task_scrollbar.set, xscrollcommand= x_task_scrollbar.set )

task_list.pack( fill="both", expand=True)


y_task_scrollbar.config(command=task_list.yview)
x_task_scrollbar.config(command=task_list.xview)


entry = ttk.Entry(window, font=("helvetica", 25))
entry.pack(pady=20)
entry.bind("<Return>", on_enter)


button_frame = ttk.Frame(window)
button_frame.pack(pady=20)

add_button = ttk.Button(button_frame, text= "Add Task", command= lambda: add_task if len(entry.get()) > 0 else None)
delete_button = ttk.Button(button_frame, text= "Delete Task", command=delete_task)
finish_button = ttk.Button(button_frame, text= "Finish Task", command=finish_task)
unfinish_button = ttk.Button(button_frame, text= "Unfinish Task", command=unfinish_task)
delete_completed_button = ttk.Button(button_frame, text="Delete Completed Tasks", command=delete_completed_tasks)
save_button = ttk.Button(button_frame, text="Save Tasks", command=save)
load_button = ttk.Button(button_frame, text="Load Tasks", command=load)



add_button.grid(row=0,column=0, padx=5)
delete_button.grid(row=0,column=1, padx=5)
finish_button.grid(row=0,column=2, padx=5)
unfinish_button.grid(row=0,column=3, padx=5)
delete_completed_button.grid(row=0, column=4, padx=5)
save_button.grid(row=2, column=2, pady = 20, padx=5)
load_button.grid(row=2, column=3, pady = 20, padx=5)






sv_ttk.set_theme("dark")



window.mainloop()









