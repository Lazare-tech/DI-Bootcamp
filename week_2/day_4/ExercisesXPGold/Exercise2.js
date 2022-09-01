function abbrevName(chaine){
    if(chaine.match(/\s\w*/)){
       
  //    let s=chaine.match(/\b(\w)/g);
    let n=chaine.match(/\s\w*/);
      let premier=chaine.match(/\S\w*/);
      let m=n.join("");
  console.log(premier+" "+m[1]);
  }
    
    
  }
  console.log(abbrevName("Robin Singh"));