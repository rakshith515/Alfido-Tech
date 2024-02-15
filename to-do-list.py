from tkinter import *

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        pass

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        pass

def delete_all_tasks():
    listbox_tasks.delete(0, END)

root = Tk()
root.title("To-Do List")

frame_tasks = Frame(root)
frame_tasks.pack()

listbox_tasks = Listbox(frame_tasks, height=15, width=50)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=50)
entry_task.pack()

button_add_task = Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_delete_all_tasks = Button(root, text="Delete all tasks", width=48, command=delete_all_tasks)
button_delete_all_tasks.pack()

root.mainloop()
