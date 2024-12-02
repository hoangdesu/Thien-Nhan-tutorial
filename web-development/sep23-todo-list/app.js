const form = document.querySelector('form');
const todosContainer = document.querySelector('#todos-container');

// array to keep track of all the TODOs
// let todoList = ['do hw', 'learn html', 'finish javascript'];

const localStorageTodoList = localStorage.getItem('todoList');
let todoList = []

if (localStorageTodoList) {
    todoList = JSON.parse(localStorageTodoList);
}

// arrow function
const renderTodoList = () => {
    todoList.forEach(task => {
        // only create an li element IN THE MEMORY
        const li = document.createElement('li');

        // asign the string to the li
        li.textContent = task;
        li.className = 'todo-item';

        // create a delete button
        const delBtn = document.createElement('button');
        delBtn.textContent = '🗑️';

        // add click event listener to the del button
        delBtn.addEventListener('click', () => {
            console.log('deleting...', task);

            // removing task
            todoList = todoList.filter(todo => todo !== task);
            
            console.log('todolist:', todoList);

            // update the new todoList inside localStorage
            localStorage.setItem('todoList', JSON.stringify(todoList));

            // reset the UI
            todosContainer.innerHTML = ''

            // render the new todo list
            renderTodoList(todoList);
        });

        // attach button to li element
        li.append(delBtn);

        // add the newly created li element into container
        todosContainer.append(li);
    });
}

// show all the todos when the app loads for the first time
renderTodoList();

form.addEventListener('submit', (e) => {
    // stop the page from reloading
    e.preventDefault(); 

    const todoInput = form.todoInput;
    console.log(todoInput.value);

    // add new todo to list, to render on the screen later
    todoList.push(todoInput.value);

    // turn the whole todo array into a string
    // and save it to local storage for later use
    localStorage.setItem('todoList', JSON.stringify(todoList));
    
    // render all the TODOs into the container
    // first wrap every todo inside an <li>todo</li>

    // clear the input
    todoInput.value = ''

    console.log(todoList);

    // reset the list before rendering a new one
    todosContainer.innerHTML = '';
    
    renderTodoList();
});