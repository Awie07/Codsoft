import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # Create frame for task list
        self.task_frame = tk.Frame(master)
        self.task_frame.pack()

        # Create listbox to display tasks
        self.task_list = tk.Listbox(self.task_frame, width=40, height=10)
        self.task_list.pack(side=tk.LEFT)

        # Create scrollbar for listbox
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=self.scrollbar.set)    
        self.scrollbar.config(command=self.task_list.yview)

        # Create entry field for new tasks
        self.new_task_entry = tk.Entry(master, width=40)
        self.new_task_entry.pack()

        # Create button to add new tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Create button to delete tasks
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        # Create button to clear all tasks
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_all)
        self.clear_button.pack()

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
        except:
            pass

    def clear_all(self):
        self.task_list.delete(0, tk.END)

root = tk.Tk()
my_gui = ToDoList(root)
root.mainloop()