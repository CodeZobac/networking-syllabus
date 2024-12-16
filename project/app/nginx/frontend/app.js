const apiUrl = "https://localhost/todos";

/**
 * Fetches the list of todos from the API and updates the DOM to display them.
 * 
 * This function sends a GET request to the API to retrieve the list of todos.
 * Once the response is received, it parses the JSON data and updates the 
 * 'todo-list' element in the DOM with the fetched todos.
 * 
 * @async
 * @function fetchTodos
 * @returns {Promise<void>} A promise that resolves when the todos have been fetched and the DOM has been updated.
 */
async function fetchTodos() {
    const response = await fetch(apiUrl, { method: 'GET', credentials: 'same-origin' });
    const todos = await response.json();
    const todoList = document.getElementById('todo-list');
    todoList.innerHTML = '';
    todos.forEach(todo => {
        const listItem = document.createElement('li');
        listItem.textContent = `${todo.id}: ${todo.title} - ${todo.description}`;
        todoList.appendChild(listItem);
    });
}

document.getElementById('todo-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const id = parseInt(document.getElementById('todo-id').value);
    const title = document.getElementById('todo-title').value;
    /**
     * Retrieves the value of the 'todo-description' input field.
     * 
     * @type {string}
     */
    const description = document.getElementById('todo-description').value;

    const todo = { id, title, description };

    await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(todo),
        credentials: 'same-origin'
    });

    fetchTodos();
});

fetchTodos();