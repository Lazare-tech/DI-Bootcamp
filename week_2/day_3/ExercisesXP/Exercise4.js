let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log("A l'etage 1 il ya "+building.numberOfAptByFloor.firstFloor+" apartements");
console.log("A l'etage 3 il ya "+building.numberOfAptByFloor.thirdFloor+" apartements");
console.log(building.nameOfTenants[1]+" room number "+building.numberOfRoomsAndRent.dan[0]);
let somme=building.numberOfRoomsAndRent.sarah[1]+building.numberOfRoomsAndRent.david[1];
if(somme>building.numberOfRoomsAndRent.dan[1]){
  building.numberOfRoomsAndRent.dan[1]+=200;
  console.log(building.numberOfRoomsAndRent.dan[1]);
}

