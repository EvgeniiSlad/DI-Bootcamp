function playTheGame() {
    let user = confirm('Press "ok" if you would like to play the game');
    if (user == true){
        var userNumber = prompt('enter a number between 0 and 10');
        checkNumber(userNumber);
    } else {
        alert ('No problem, Goodby');
    }
}

function  checkNumber(userNumber) {
    if (isNaN(userNumber) == true) {
        alert ('Sorry Not a number, Goodbye');
        return;
    } else if (10 < userNumber || userNumber < 0) {
        alert ('Sorry it’s not a good number, Goodbye');
        return;
    } else if (0 <= userNumber && userNumber <= 10) {
        var computerNumber = Math.trunc(Math.random()*10);
        console.log(computerNumber);
        compareNumbers(userNumber,computerNumber);
    }
}

function compareNumbers(userNumber,computerNumber)  {
    let chances = 1
    do {
        if (userNumber == computerNumber){
            alert ('WINNER!');
            return;
        } else if (userNumber > computerNumber){
            userNumber =  Number(prompt('Your number is bigger then the computer’s, guess again!'));
        } else if (userNumber < computerNumber){
            userNumber =  Number(prompt('Your number is smaller then the computer’s, guess again!'));
        }
        chances++
    } while (chances < 3)
    alert('Out of chances! Sorry');
}

playTheGame();