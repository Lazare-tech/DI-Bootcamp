let age = [20,5,12,43,98,55];
let somme=0;
let ageHighest=0;
for(let x in age){
     somme=somme+age[x];
if(ageHighest<age[x]){
        ageHighest=age[x];
        
    }
}
console.log(somme);
console.log("The highest age is "+ageHighest);
