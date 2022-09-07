
const x=document.getElementsByTagName("h1");
console.log(x[0].textContent);
const p=document.getElementsByTagName("p");
p[3].remove();
document.getElementsByTagName("h2")[0].onclick=function(){
    document.getElementsByTagName("h2")[0].style.backgroundColor="red";

};
document.getElementsByTagName("h3")[0].onclick=function(){
    document.getElementsByTagName("h3")[0].style.display="none";

};
document.getElementById("button").onclick = function(){
    document.body.style.fontWeight="bold";

};
// Returns a random integer from 0 to 9:
document.getElementsByTagName("h1")[0]. onmouseover=function(){
    const n=Math.floor(Math.random() * 100); 
    document.getElementsByTagName("h1")[0].style.fontSize=n+'px';

};

