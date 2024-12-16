from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None

# In-memory database
todo_db: List[TodoItem] = []

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    """
    Retrieve the list of todos from the database.

    Returns:
        list: A list of todo items from the database.
    """
    return todo_db

@app.post("/todos", response_model=TodoItem, status_code=201)
def create_todo(todo: TodoItem):
    """
    Adds a new todo item to the todo database.

    Args:
        todo (TodoItem): The todo item to be added.

    Raises:
        HTTPException: If an item with the same ID already exists in the database.

    Returns:
        TodoItem: The added todo item.
    """
    if any(item.id == todo.id for item in todo_db):
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    todo_db.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, todo: TodoItem):
    """
    Update an existing todo item in the todo database.

    Args:
        todo_id (int): The ID of the todo item to update.
        todo (TodoItem): The new todo item data.

    Returns:
        TodoItem: The updated todo item.

    Raises:
        HTTPException: If the todo item with the specified ID is not found.
    """
    for index, item in enumerate(todo_db):
        if item.id == todo_id:
            todo_db[index] = todo
            return todo
    raise HTTPException(status_code=404, detail="Item not found.")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    """
    Deletes a todo item from the todo_db based on the provided todo_id.

    Args:
        todo_id (int): The ID of the todo item to be deleted.

    Raises:
        HTTPException: If the todo item with the specified ID is not found, 
                       an HTTP 404 exception is raised with the message "Item not found."
    """
    for index, item in enumerate(todo_db):
        if item.id == todo_id:
            del todo_db[index]
            return
    raise HTTPException(status_code=404, detail="Item not found.")