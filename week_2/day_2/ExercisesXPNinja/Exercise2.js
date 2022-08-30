let code=prompt("Entrer zip code");

if(code.match(/\d{1,5}/) && code.match(/\S/) && code.match(/[0-9]/) )
{
    console.log("success");
}
else{
    console.log("error");
}
