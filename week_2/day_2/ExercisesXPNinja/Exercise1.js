let naiss1=parseInt(prompt("Donnez votre date de naissance?"));
let naiss2=parseInt(prompt("Donnez votre date de naissance?"));
if(naiss1>naiss2){
    let result1=2022-naiss1;
    let result2=2022-naiss2;
    let moitie=result1/2;
    let age2=result1-moitie;
    console.log(age2);
}
else if(naiss1<naiss2){
    let result1=2022-naiss1;
    let result2=2022-naiss2;
    let moitie=result2/2;
    let age1=result1-moitie;
    console.log(age1);

}