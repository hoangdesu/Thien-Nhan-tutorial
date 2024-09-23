const form = document.querySelector('form');
const todosContainer = document.querySelector('#todos-container')

// array to keep track of all the TODOs
const todoList = [];

form.addEventListener('submit', (e) => {
    // stop the page from reloading
    e.preventDefault(); 

    const todoInput = form.todoInput;
    console.log(todoInput.value);

    // add new todo to list, to render on the screen later
    todoList.push(todoInput.value);
    
    // render all the TODOs into the container
    // first wrap every todo inside an <li>todo</li>

    // clear the input
    todoInput.value = ''

    console.log(todoList);

    // reset the list before rendering a new one
    todosContainer.innerHTML = '';
    
    todoList.forEach(task => {
        // only create an li element IN THE MEMORY
        const li = document.createElement('li');

        // asign the string to the li
        li.textContent = task;

        // add the newly created li element into container
        todosContainer.append(li);
    });

});