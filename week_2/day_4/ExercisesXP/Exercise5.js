let somme=0,quarter,dimes,nickel,penny;
function changeEnough(itemPrice, amountOfChange=[]){
        quarter=amountOfChange[0]*0.25;
        dimes=amountOfChange[1]*0.10;
        nickel=amountOfChange[2]*0.05;
        penny=amountOfChange[3]*0.02;
        somme=quarter+dimes+nickel+penny;
    
    if(somme>=itemPrice){
        return true;

    }
    else if(somme<itemPrice){
        return false;
    }
}
// changeEnough(4.25, [25, 20, 5, 0]);//return true
// changeEnough(14.11, [2,100,0,0]);//return false
changeEnough(0.75, [0,0,20,5]) //returns true