document.addEventListener('DOMContentLoaded', function() {
    const addSuggButton = document.getElementById('addsuggButton');
    const addSuggInputBox = document.getElementById('addSugg');

    addSuggButton.addEventListener('click', function() {
        const newLi = document.createElement('li');
        newLi.textContent = "Thank you for the suggestion, we will work on it!!!";
        newLi.classList.add('textColor');
        newLi.classList.add('textDecor');
        document.querySelector('main').appendChild(newLi);
    });
});
