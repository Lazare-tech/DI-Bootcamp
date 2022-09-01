//: Words in the stars
let chaine=prompt("Entrer une chaine de caractere separe par des virgules");
let convert=chaine.split(",");
let n="*",c=0,long=0,espace=" ";
console.log(convert);
 for (i=0; i<convert.length; i++){
      if (convert[i].length > long){
        long= convert[i].length;
      }

  }
console.log(long);
console.log(n.repeat(long));
for(let i=0;i<convert.length;i++){
//   if(convert[i].length>convert[i+1].length){
    console.log("* "+convert[i]+espace.repeat()+"*");
//   }
	

}
console.log(n.repeat(long+4));



