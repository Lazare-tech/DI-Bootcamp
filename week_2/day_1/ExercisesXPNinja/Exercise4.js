let number=parseInt(prompt("Enter a number"));
let chaine;
if (number<2)
{
    alert(chaine);
}

else if (number%2!==0 && number>2){
    chaine="b"+'o'.repeat(number)+"m";
    alert(chaine)
}

else if (number%2==0 && number>2){
    chaine="b"+'o'.repeat(number)+"m!";
    alert(chaine)
}
else if (number%5==0){
    chaine="b"+'o'.repeat(number)+"m";
    alert(chaine.toUpperCase(chaine));
}
else if(number%2==0 && number%5==0)
{
    chaine="b"+'o'.repeat(number)+"m!";
    alert(chaine.toUpperCase(chaine));
}