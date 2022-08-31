let gradesList=[12,10,19,17,14];
let total=0;

function findAvg(gradesList){
  	totalnote();
  moyenne();
   
    }
 
function totalnote(){
    for(let i=0;i<gradesList.length;i++){
        total=total+gradesList[i];
    }
}
function moyenne(){
    totalnote();
    moyenne=total/gradesList.length;
    if(moyenne>65){
      console.log("success!");
    }
    else{
          console.log("failed,you must repeat the course");
  
    }
}
findAvg(gradesList);