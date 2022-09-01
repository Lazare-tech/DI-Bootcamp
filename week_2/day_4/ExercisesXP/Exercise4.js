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
//function
let totalPrice=0;
function  myBill(){
    for(let i in shoppingList){
    if(shoppingList[i] in stock){
        
        //  totalPrice = totalPrice+prices.shoppingList[i];
        console.log(prices.i);

    }
}
// console.log(totalPrice);
}
myBill();