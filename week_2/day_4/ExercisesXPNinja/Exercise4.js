let x=0,i;

function biggestNumberInArray(arrayNumber){
   for(i=0;i<arrayNumber.length;i++){
        if(arrayNumber[i] > x){
            x=arrayNumber[i];
        }
    }
              return x;

}
biggestNumberInArray(arrayNumber)([-1,0,3,100, 99, 2, 99]);
// const array2 = ['a', 3, 4, 2]; // should return 4 