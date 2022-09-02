//99 Bottles of Beer
let chiffre=parseInt(prompt("Donnez un nombre"));
for(let i=chiffre;i>0;i++){
    for(let y=1;y<=i;y++){
    chiffre=chiffre-y;
      if(y==1){
        alert("on prend "+y+" en bas on la fait circuler");
        alert("nous avons maintenant "+chiffre+" bouteilles");
      }else
        {
           alert("on prend "+y+" en bas on les fait circuler");
           alert("nous avons maintenant "+chiffre+" bouteilles");
        }
    }
}