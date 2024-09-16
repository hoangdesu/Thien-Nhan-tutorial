// console.log('hello from javascript');

let counter = 1;

// step 1: access the element(s) that you want to manipulate
const counterSpan = document.querySelector('#counter');
// console.dir(counterSpan);

// select 2 buttons
const minusBtn = document.querySelector('#minus');
const plusBtn = document.querySelector('#plus');


// bind an event listener to the selected buttons
plusBtn.addEventListener('click', () => {

    if (counterSpan.style.color === 'red')
        counterSpan.style.color = 'black';

    counter++; // only update inside memory
    console.log('counter:', counter);

    // i want to update the DOM as well!
    counterSpan.textContent = counter;
})

minusBtn.addEventListener('mouseleave', () => {
    if (counter === 0) {
        counterSpan.style.color = 'red';
        return;
    }

    counter--; // only update inside memory
    console.log('counter:', counter);

    // i want to update the DOM as well!
    counterSpan.textContent = counter;
})



// step 2: change its values