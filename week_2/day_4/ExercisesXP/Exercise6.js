let nombreJourLouerVoiture;
function hotelCost(nombreNuit) {
    return "l'hotel a coute : " + 140 * nombreNuit + "$";
}

//second function
function planeRideCost(destination) {
    let londres = 183, paris = 220, otherDestination = 300;
    if (destination === "londres") {
        return "Les billets d'avion ont coute :" + londres + "$";
    }
    else if (destination === "paris") {
        return "Les billets d'avion ont coute :" + paris + "$";


    }
    else {
        return "Les billets d'avion ont coute :" + otherDestination + "$";

    }
}
//third function
function rentalCarCost(nombreJourLouerVoiture) {
    let coutLocation = 40 * nombreJourLouerVoiture;
    if (nombreJourLouerVoiture > 10) {
        let remise = (coutLocation * 5) / 100;
        return "La voiture a coute :" + remise + "$";

    }
    else {
        return "La voiture a coute :" + coutLocation + "$";

    }
}
//fourth function
function totalVacationCost() {
    do {

        nombreNuit = parseInt(prompt("Donnez le nombre de nuit que vous voules passer a l'hotel"));

    } while (!Number(nombreNuit));
    
    do {
        destination = prompt("Donnez votre destination");
    } while (Number(destination));

    do {
         nombreJourLouerVoiture = parseInt(prompt("Pendant combien de jours vous voulez louer une voiture"));
    } while (!Number(nombreJourLouerVoiture));
    console.log(hotelCost(nombreNuit) + ", " + planeRideCost(destination) + "," + rentalCarCost(nombreJourLouerVoiture));
}
totalVacationCost();