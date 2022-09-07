let x = document.getElementById("btn");
x.addEventListener("mouseout",RespondMouseout);
x.addEventListener("mouseover",RespondMouseover);
x.addEventListener("dblclick",RespondDbclick);

let bg;
function RespondMouseout()
{
     bg=document.body.firstElementChild;
    bg.style.backgroundColor="red";
}
function RespondMouseover()
{
    bg=document.body.firstElementChild;
    bg.style.border="2px solid red";
}
function RespondDbclick()
{
    bg.style.fontStyle="italic";
}