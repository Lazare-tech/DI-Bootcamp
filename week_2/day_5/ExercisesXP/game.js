//Play a guessing game
let reponse, nombre, computerNumber;
function playTheGame() {
    reponse = confirm('Souhaitez vous jouer au jeu?');
    if (reponse) {
        alert("Entrer un nombre");
        nombre = prompt("Entrer un nombre");
        if (Number(nombre)) {
            if (nombre > 10) {
                alert("Sorry it's not a good number, Goodbye");
            }
            else {
                computerNumber = Math.floor(Math.random() * 10);
                alert(computerNumber);
                compareNumbers(nombre, computerNumber);
            }

        } else {
            alert('Sorry Not a number, Goodbye');
        }

    } else {
        alert('No problem, Goodbye');
    }
}
//function comparenumber

function compareNumbers(nombre, computerNumber) {
    let chance = 3;
    while (chance >0) {
        if (nombre == computerNumber) {
            alert("WINNER");
            chance = -1;
        }

        else if (nombre > computerNumber) {
            chance=chance-1;
            do {

                alert("Votre numéro est plus grand que celui de l'ordinateur, essayez à nouveau");
                alert("entrer un nombre");
                nombre = parseInt(prompt("Entrer une nombre"));
            } while((!nombre && nombre!=0 ) || nombre>0 && nombre<10);
        } else if (nombre < computerNumber){
            chance=chance-1;

            do {
                alert("Votre numéro est plus petit que celui de l'ordinateur, essayez à nouveau");


                alert("entrer un nombre");
                nombre = parseInt(prompt("Entrer une nombre"));
            } while((!nombre && nombre!=0 ) || nombre>0 && nombre<10);

        }
    }


}

playTheGame();

