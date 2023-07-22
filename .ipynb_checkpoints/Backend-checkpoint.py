todos_list = []

while True:
    task = input("type new, edit, complite, show: ").strip()
    if task == "new":
        newTodo = input('type your new todo: ').strip()
    
        with open('todos.txt', 'a') as file:
                file.writelines(newTodo + '\n')

    elif task == "show":
        with open('todos.txt', 'r') as file:
                todos_list = file.readlines() 
        for index,item in enumerate(todos_list):
            print(f"{index+1} {item.strip()}") #readline added \n so we use .stip() to remove it 
        break





            
