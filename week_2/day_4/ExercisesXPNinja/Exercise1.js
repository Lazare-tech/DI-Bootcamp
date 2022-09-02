// Random Number
let x,n=[];
function getRandomInt(max) {
  	
    x=Math.floor(Math.random() * max);
  console.log("Le nombre aleatoire est "+x);
  console.log("Les nombres paires jusqu'au nombre aleatoire sont:");
  for(let i=0;i<=x;i++){
	if(i%2==0){
  console.log(i);
  }
  }
  return ;
}

console.log(getRandomInt(100));
  