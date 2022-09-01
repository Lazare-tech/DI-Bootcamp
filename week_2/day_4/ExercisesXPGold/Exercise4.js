// Omnipresent value
function isOmnipresent(tab=[],value){
    for(let i=0;i<tab.length;i++){
        for(let y=0;y<tab.length;y++){
        if(value != tab[i][y]){
          console.log(value+" does not exists in every element inside this array, so is not omnipresent.");
          
          break;
           
        }
          else
            {
               console.log(value+ " exists in every element inside this array, so is omnipresent.");break;
            }
    }break;
    }
  
        


}
isOmnipresent([[1, 1], 
    [1, 3],
     [5, 1],
      [6, 1]], 
      1);//true
    //   isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) //false