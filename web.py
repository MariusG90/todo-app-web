import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo_text = st.session_state["new_todo"].strip()
    if todo_text:
        todos.append(todo_text + "\n")  # add newline for the file
        functions.set_todos(todos)
        st.session_state["new_todo"] = ""

st.title("My Todo App")

for index, todo in enumerate(todos):
    todo_clean = todo.rstrip("\n")
    checkbox = st.checkbox(todo_clean, key=f"{todo_clean}_{index}")
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        st.rerun()

st.text_input(
    label=" ",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)