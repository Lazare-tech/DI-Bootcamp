let form=document.body.firstElementChild.nextElementSibling;
console.log(form);
//......................................
let bouton=document.getElementById("lib-button");
bouton.addEventListener("click",test)

function test(event){
    let noun=document.getElementById("noun").value ;
    let adjective=document.getElementById("adjective").value ;
    let personn=document.getElementById("person").value ;
    let verbe=document.getElementById("verb").value ;
    let place=document.getElementById("place").value ;
    //...................................
    if(noun!="" && adjective!="" && person!="" && verbe!="" && place!="" )
{
    let i=document.body.firstElementChild.nextElementSibling;
    let u=i.nextElementSibling.firstElementChild;
    let v=document.createTextNode('Je me nomme '+noun+" je suis super "+adjective+" sans doute "
    +" je suis une "+personn+" "+verbe+" dans une hisoire de "+place);
    u.appendChild(v);
    console.log(v);    
}
event.preventDefault();
};
//...................................

let hist=['histoire1','histoire2','histoire3'];

let s=document.getElementById("shuffle-button");
// bouton.addEventListener("click",test);
s.addEventListener("click",shuffle);
function shuffle(event){
    let noun=document.getElementById("noun").value ;
    let adjective=document.getElementById("adjective").value ;
    let personn=document.getElementById("person").value ;
    let verbe=document.getElementById("verb").value ;
    let place=document.getElementById("place").value;

    if(noun!="" && adjective!="" && personn!="" && verbe!="" && place!="" )
{
    
    //..................................
    let histoire1=document.createTextNode('Je me suis  '+noun+" je suis unr "+adjective+" sans doute  mon amie se nomme  "+personn+"et "+verbe+" qui est a "+place);
let histoire2=document.createTextNode('Mon surnom est  '+noun+" et je suis un vrai "+adjective+" sans doute "
+" mon vrai surnom est "+personn+"et je"+verbe+" tres bien quand je suis a "+place);
let histoire3=document.createTextNode('Salut ici,je me presente  '+noun+" vous etes "+adjective+" cest genial "
+" vous pouvez mapellez"+personn+"je"+verbe+" je suis vers "+place);
    //
    let n=Math.floor(Math.random() * 2); 
    let x=document.body.firstElementChild.nextElementSibling;
    let y=x.nextElementSibling.firstElementChild;
    switch(n){
        case 0:
            y.appendChild(histoire1).textContent;
            break;
            case 1:
                y.appendChild(histoire2);
                case 3:
                    y.appendChild(histoire2);
                        break;
                        default:


    }
    event.preventDefault();
}

}

