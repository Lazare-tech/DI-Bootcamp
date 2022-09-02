//: Words in the stars
let chaine=prompt("Entrer une chaine de caractere separe par des virgules");
let convert=chaine.split(",");
let n="*",c=0,long=0;
console.log(convert);
 for (i=0; i<convert.length; i++){
      if (convert[i].length > long){
        long= convert[i].length;
      }

  }
console.log(long);
console.log(n.repeat(long+5));
for(let i=0;i<convert.length;i++){
  let marge=(long+1)-convert[i].length;
  let espace=" ";

  for(let i=0;i<marge;i++){
    espace=espace+" ";
    
  }
//   if(convert[i].length>convert[i+1].length){
    console.log("* "+ convert[i] + espace+"*");
}

	


console.log(n.repeat(long+5));



