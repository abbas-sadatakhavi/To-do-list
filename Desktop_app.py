import Functions
import PySimpleGUI as sg

# Create GUI elements
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=Functions.openFile(), key="todos", enable_events=True, size=(45, 10)
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

# Create the window layout
layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button]]

# Create the window
window = sg.Window("My To-Do App", layout, font=("Helvetica", 20))
# event, values = window.read()


while True:
    event, values = window.read()
    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])

    # Handle events
    if event == "Add":
        try:
            todos = Functions.openFile()
            if values["todo"] == "":
                continue
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("write new to do")

    elif event == "Edit":
        try:
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = Functions.openFile()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
        except IndexError:
            sg.popup("select item to edit")

    elif event == "Complete":
        try:
            todo_to_complete = values["todos"][0]
            todos = Functions.openFile()
            todos.remove(todo_to_complete)
            Functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        except IndexError:
            sg.popup("select item to complete")
    elif event == "todos":
        try:
            window["todo"].update(value=values["todos"][0])
        except IndexError:
            sg.popup("write new to do")

    elif event == sg.WIN_CLOSED:
        break

window.close()
