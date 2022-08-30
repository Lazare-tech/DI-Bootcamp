let code=parseInt(prompt("Entrer zip code"));

if(code.length<=5 && isNum(code) )
{
    console.log("success");
}
else{
    console.log("error");
}
