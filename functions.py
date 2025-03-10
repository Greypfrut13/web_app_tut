FILEPATH = "todos.txt"

def save_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos)

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local
