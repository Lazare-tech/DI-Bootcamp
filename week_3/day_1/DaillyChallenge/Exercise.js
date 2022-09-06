let tab=['Mercure','Venus','Terre','Mars','Jupiter','Saturne',
'Uranus','Neptune','Pluton'];
let couleur=['green','yellow','Blue','red','gray','orange','indigo','black','chocolate'];
let moon=[2,3,1];
//jpiter 79 uranus 19
// for(let i=0;i<tab.length;i++){
   
//   const y=document.createTextNode(tab[0]);
 for(let i=0;i<tab.length;i++){
   const x=document.createElement("div");
   const m=document.createElement("p2");
    const p=document.createElement("p");
    const y=document.createTextNode(tab[i]);
    x.appendChild(p);
    x.appendChild(m);
    p.appendChild(y);
    p.style.color='white';
    document.body.firstElementChild.appendChild(x);
 document.getElementsByTagName("div")[i].classList.add( "planet");
 document.getElementsByTagName("p2")[i].classList.add( "moon");

 document.getElementsByTagName("div")[i].style.backgroundColor=couleur[i]; 
 }
 

