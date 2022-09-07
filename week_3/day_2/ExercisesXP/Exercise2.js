let form=document.forms[0];
console.log(form);
let elementName1=form.elements.fname;
let elementName2=form.elements.lname;

console.log(elementName1);
console.log(elementName2);
document.getElementById("submit").addEventListener("click",
function(event){
event.preventDefault();
});

// const text=document.createTextNode();
// liste1.appendChild(text);


let fname=document.getElementById("fname").value ;
let lname=document.getElementById("lname").value ;

console.log(fname);
if(fname=="" && lname==""){
    alert("vide");
    
}else{
    const liste1=document.createElement("li");
    const liste2=document.createElement("li");
    const c=document.body.firstElementChild.nextElementSibling;
    c.appendChild(liste1);
c.appendChild(liste2);
const text=document.createTextNode(fname);
liste1.appendChild(text);
const textt=document.createTextNode(lname);
liste2.appendChild(textt);

}


