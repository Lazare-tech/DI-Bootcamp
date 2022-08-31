let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people.push("yelmani");
console.log(people.indexOf('Mary'));
let newPeople=people.slice(1,4);
let copyAllPeople=people.slice(0,4);
console.log(people.indexOf("Foo"));//it return -1
let taille=people.length;
let last=people[taille-1];
//length donne le nombre delement present dans le tableau
//indexOf donne la position de lelement dans le tableau,on commence a compter a partir de wero
//PART II
for(let x in people){
    console.log(people[x]);
}
for(let x in people){
    if( people[x]=="Devon");
    console.log(people[x]);

    break;
}