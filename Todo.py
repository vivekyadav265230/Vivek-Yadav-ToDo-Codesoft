from tkinter import Tk, Label, Entry, Button, Listbox

class TodoItem:
  def __init__(self, description):
    self.description = description
    self.completed = False

class ToDoListApp:
  def __init__(self, master):
    self.master = master
    master.title("To-Do List")
    master.geometry("500x300")
    

    self.todo_list = []
    self.task_label = Label(master, text="Task:")
    self.task_label.pack()

    self.task_entry = Entry(master)
    self.task_entry.pack(padx=10, pady=5)

    self.add_button = Button(master, text="Add Task", command=self.add_task)
    self.add_button.pack(pady=5)

    self.listbox = Listbox(master)
    self.listbox.pack(fill="both", expand=True)
    self.listbox.bind("<Double-1>", self.mark_completed) 

    self.complete_button = Button(master, text="Mark Completed", command=self.mark_selected)
    self.complete_button.pack(pady=5)

    self.remove_button = Button(master, text="Remove Task", command=self.remove_selected)
    self.remove_button.pack(pady=5)

  def add_task(self):
    """Adds a new task to the list and updates the listbox."""
    description = self.task_entry.get()
    if description:
      self.todo_list.append(TodoItem(description))
      self.listbox.insert("end", description)
      self.task_entry.delete(0, "end")  

  def mark_completed(self, event):
    """Marks the selected task as completed and updates the listbox."""
    selected_index = self.listbox.curselection()
    if selected_index:
      index = int(selected_index[0])
      self.todo_list[index].completed = True
      self.update_listbox()

  def mark_selected(self):
    """Marks the selected task(s) as completed and updates the listbox."""
    for index in self.listbox.curselection()[::-1]:  
      self.todo_list[int(index)].completed = True
    self.update_listbox()

  def remove_selected(self):
    """Removes the selected task(s) from the list and listbox."""
    for index in self.listbox.curselection()[::-1]:
      del self.todo_list[int(index)]
    self.update_listbox()

  def update_listbox(self):
    """Clears and repopulates the listbox with updated task information."""
    self.listbox.delete(0, "end")
    for item in self.todo_list:
      status = "Completed" if item.completed else "Pending"
      self.listbox.insert("end", f"{status}: {item.description}")

root = Tk()
app = ToDoListApp(root)
root.mainloop()
