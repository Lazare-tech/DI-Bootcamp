let form=document.body.firstElementChild.nextElementSibling;
document.getElementById("submit").addEventListener("click",
function(event){
    let radius=document.getElementById("radius").value ;
    let volume=((4*3.14)*radius*radius*radius)/3;
    if(radius!=""){
    console.log(radius);
    console.log(volume);
        let vol=document.getElementById("volume");
        vol.value=volume;
    }

event.preventDefault();
});