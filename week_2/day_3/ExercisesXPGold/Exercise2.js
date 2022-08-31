let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  };

  let nom=prompt("Enter your name");
    if(nom in guestList){
        console.log("Hi! I'm "+nom+", and I'm from "+guestList[nom]+" country");
    }
    else{
        console.log("Hi! I'm a guest.");
    }
  