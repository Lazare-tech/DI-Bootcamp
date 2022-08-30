let verbe=prompt("Quel est votre grade?");
if(verbe.length>=3 && !verbe.match(/ing\b/))
{
    let newVerbe=verbe+"ing";
    console.log(newVerbe);
}
else if(verbe.length>=3 && verbe.match(/ing$/))
{
    let newVerbe=verbe+"ly";
    console.log(newVerbe);

}
else if(verbe.length<3)
{
    console.log(verbe);
}