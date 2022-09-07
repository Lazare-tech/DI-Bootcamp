//Move the box
function myMove()
{
    var element=document.getElementById("animate");
    var pos=0;
    var id=setInterval(frame,5);
    function frame()
    {
        if(pos==345){
            clearInterval(id);
        }
        else{
            pos++;
            element.style.left=pos+"px";
        }
    }
}
