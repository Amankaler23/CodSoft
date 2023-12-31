import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x700")
root.resizable(False,False)
task_list = []
def addTask():
    task= task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("c:/Users/iPC/Pictures/tasklist.txt.txt","a")as taskfile:
            taskfile.write(f"/n{task}")
        task_list.append(task) 
        listbox.insert(END,task)  
def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("c:/Users/iPC/Pictures/tasklist.txt.txt","w") as taskfie:
            for task in task_list:
                taskfie.write(task+"/n")
        listbox.delete(ANCHOR)        

def openTaskFile():
    global task_list
    
    try:
        with open("c:/Users/iPC/Pictures/tasklist.txt.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task.strip():  # This will check if the task is not just a newline
                    task_list.append(task)
                    listbox.insert(END, task)
    except FileNotFoundError:
        file = open("c:/Users/iPC/Pictures/tasklist.txt.txt", "w")
        file.close()


# icon
Image_icon = PhotoImage(file="c:/Users/iPC/Pictures/Saved Pictures/task.png")
root.iconphoto(False, Image_icon)

# top bar
Top_Image = PhotoImage(file="c:/Users/iPC/Pictures/Saved Pictures/topbar.png")
Label(root, image=Top_Image).pack()

dockImage = PhotoImage(file="c:/Users/iPC/Pictures/Saved Pictures/dock.png")
Label(root, image=dockImage, bg="#32405b").place(x=30, y=25)

noteImage = PhotoImage(file="c:/Users/iPC/Pictures/Saved Pictures/task.png")
Label(root, image=noteImage, bg="#32405b").place(x=30, y=25)

heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=150)

task = StringVar()
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=300, y=0)

# listbox
frame1= Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=16 , bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

#delete
Delete_icon=PhotoImage(file="c:/Users/iPC/Pictures/Saved Pictures/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,padx=35,pady=35)
root.mainloop()
