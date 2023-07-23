def openFile():
    with open("todos.txt", "r") as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(newtodo):
    with open("todos.txt", "w") as file:
        file.writelines(newtodo)
