// Show only the letters
let x=document.getElementById("text").value ;
let tt=[];
function myFunction(){
   
    for(let i=0;i<x.length;i++){
        let l=x[i];
        if(Number(l) || l=='.' || l=='/' || l=='?' || l=='#' || l=='&' || l=='*' ){
            x[i]=" ";
        }
        else
        {
            tt=x[i];
            

          
        }
        alert("Les bonnes caracetres sont :"+tt);



        
    }

}
    


    


