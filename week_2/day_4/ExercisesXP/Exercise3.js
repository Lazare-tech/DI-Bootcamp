let somme=0;
function  isDivisible(divisor){
    for(let i=0;i<=500;i++){
        if(i%divisor==0){
            console.log(i);
            somme=somme+i;
        }
    }
    console.log("Somme "+somme);

}
//a parameter divisor to the function.
isDivisible(23);