document.getElementsByTagName("li")[1].innerHTML="Richard";
const n=document.getElementsByTagName("li");

// document.getElementsByTagName("li")[0].innerHTML="Lazare";
// document.getElementsByTagName("li")[2].innerHTML="Lazare";
for(let i=0;i<n.length;i++){
  if(i==0)
    {
      document.getElementsByTagName("li")[i].innerHTML="Lazare";

    }else if(i==2)
      {
        document.getElementsByTagName("li")[2].innerHTML="Lazare";

        
      }
  else if(i==3)
    {
              document.getElementsByTagName("li")[3].remove();

    }
}
