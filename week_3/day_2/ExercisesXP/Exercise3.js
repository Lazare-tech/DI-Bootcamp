let allBoldItem=[];
function getBold_items() {
    document.getElementsByTagName("p");
   let taille= document.getElementsByTagName("strong").length;
   console.log(taille);
   for(let i=0;i<taille;i++){
    allBoldItem=document.getElementsByTagName("strong")[i].innerHTML;
    console.log(allBoldItem);

   }
    
}
getBold_items();
function highlight()
{
    for(let i=0;i<6;i++){

    document.getElementsByTagName("strong")[i].style.color="blue";
    }
    
}
function return_normal()
{
        for(let i=0;i<6;i++){
        document.getElementsByTagName("strong")[i].style.color="black";
        }
}
let v=document.body.firstElementChild;
v.setAttribute("onmouseover","highlight()");
v.setAttribute("onmouseout","return_normal()");

// document.getElementsByTagName("strong").onmouseout=return_normal();

// return_normal();
// highlight();
