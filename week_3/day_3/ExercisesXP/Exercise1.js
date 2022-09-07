let firstElement=document.body.firstElementChild;
let p,text,n=5;
function hello(){
    //PART I
    alert("Hello World");
    //PART II
    p =document.createElement("p");
     text=document.createTextNode("Hello world");
    p.appendChild(text);
    firstElement.appendChild(p);
    
    
  
}
setTimeout(hello,2000);
//part III
const timer=setInterval(afficher,2000);
function afficher(){
      
      
      if(n!=0){

      p =document.createElement("p");
      text=document.createTextNode("Hello world");
     p.appendChild(text);
    firstElement.appendChild(p);
    n=n-1;
      }

};
document.getElementById("clear").onclick=function(){
    clearInterval(timer);
}
