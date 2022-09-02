let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  ;

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} ;
let shoppingList=["banana","orange","apple"];
let somme=0;
//function
let totalPrice=0;
function  myBill(){
    for(let i in shoppingList){
        for(let j in stock){
    if(shoppingList[i] ==j && stock[j]!=0 ){   
        for(let p in prices){
            if(p==j){
                somme= somme+prices[p];
                stock[j]=stock[j]-1;
            }
        }
        
    }

    }
}
console.log("La somme des fuits est "+somme);
// console.log(totalPrice);
}
myBill();