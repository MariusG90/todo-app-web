FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of to-do items. """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def set_todos(todos, filepath=FILEPATH):
    """ Write the to-do items in a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos)