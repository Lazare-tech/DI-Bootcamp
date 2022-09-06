document.body.firstElementChild.setAttribute("id","socialNetworkNavigation");
const u=document.body.firstElementChild.nextElementSibling;

const list=document.getElementsByTagName("li");
const first=document.createElement("li");
const element=document.createTextNode("Logout");
// first.appendChild(element);
 first.appendChild(element);
document.getElementById("socialNetworkNavigation").firstElementChild.appendChild(first);
        // document.getElementsByTagName("ul")[0].textContent=list[0].textContent;
// for(let i=0;i<list.length;i++){
    let i=4;
    while(i!=0){ 
    let x=document.getElementsByTagName("ul")[0];
     x=list[i].style.display='none';
     
       i--; 
    }
// }
        // document.getElementsByTagName("ul")[0].textContent=list[1].textContent;
