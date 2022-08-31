const numbers = [5,0,9,1,7,4,2,6,3,8];
let convertToString=numbers.toString();
let convertWithJoin=numbers.join("");
numbers.sort((a,b) => b-a);
console.log(numbers);
let temp=numbers[0],newTab;
for(let i in numbers){
    if(temp>numbers[i+1]){
         newTab=[temp];
    }
}
console.log(newTab);