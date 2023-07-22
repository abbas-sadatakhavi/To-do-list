import Functions

todos_list = []


while True:
    task = input("type new, edit, complete, show: ").strip()
    if task == "new":
        newTodo = input("type your new todo: ").strip()

        with open("todos.txt", "a") as file:
            file.writelines(newTodo + "\n")

    elif task == "show":
        todos_list = Functions.openFile()
        for index, item in enumerate(todos_list):
            print(
                f"{index+1} {item.strip()}"
            )  # readline added \n so we use .stip() to remove it

    elif task == "edit":
        try:
            i = int(input("type number"))
            edited_todo = input("type edited to do ").strip()
            todos_list = Functions.openFile()

            todos_list[i - 1] = edited_todo + "\n"
            with open("todos.txt", "w") as file:
                file.writelines(todos_list)
        except IndexError:
            print("there is no such index")
            continue

    elif task == "complete":
        i = int(input("type number"))
        todos_list = Functions.openFile()
        todos_list.pop(i - 1)
        with open("todos.txt", "w") as file:
            file.writelines(todos_list)
