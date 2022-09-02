// Unique Elements
let i,newList;
function uniqueElements(list){
    for(i=0;i<list.length;i++){
        if(list[i].repeat(2))
        {
            newList=list[i].repeat(i);
        }
        return newList;
    }
}
uniqueElements([1,2,3,3,3,3,4,5]);