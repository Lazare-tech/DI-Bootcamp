let montant,pourboire,total;
function calculateTip(){
    montant=parseInt(prompt("Entrer le montant de l'addition"));
    if(montant<50){
        pourboire=20;
        total=montant+(pourboire/100);
        console.log("Le pourboire fait "+pourboire+"%");
        console.log("L'addition final est "+total);
        }
        else if(montant>50 && montant<200){
            pourboire=15;
            total=montant+(pourboire/100);
            console.log("Le pourboire fait "+pourboire+"%");
            console.log("L'addition final est "+total);

        }
        else if(montant>200){
            pourboire=10;
            total=montant+(pourboire/100)
            console.log("Le pourboire fait "+pourboire+"%");
            console.log("L'addition final est "+total);

        }
}
//call function
calculateTip();