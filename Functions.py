def openFile():
    with open("todos.txt", "r") as file:
        todos_list = file.readlines()
    return todos_list
