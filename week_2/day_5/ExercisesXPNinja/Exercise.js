let y=10,taille;
let motTrouver=[];
let mot=prompt("Entrer un mot");
taille=mot.length;
let array=new Array(taille);
for(let u=0;u<taille;u++){
  array[u]="*";
}
console.log(mot);
while(y>=0){
  let newMot=prompt("Entrer une lettre");
for(let i=0;i<mot.length;i++){
  if(mot[i]==newMot){
    array[i]=mot[i];
//       if(array[i]===undefined){
//       array[i]="*";
//       }
    
motd=array.join("");
//     let a = motd;
 console.log(motd);
//     console.log(a);
  if(motd==mot){
    console.log(" CONGRATS YOU WIN");
   	y=-1;
  }
     if(y==0)
      {
        // console.log("le mot"+newMot+" ala postion"+i+"du mot"+mot);
       
        console.log("YOU LOSE");
      }
        
      
  }
  
}
y--;

}