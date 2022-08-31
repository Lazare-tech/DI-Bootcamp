let firstPerson={
    Fullname: 'jonh',
    Mass: 56,
    Heigth:1.35,
    bmi: function(){
        return this.Mass/this.Heigth;
    }
};
let secomdPerson={
    Fullname: 'charle',
    Mass: 65,
    Heigth:2.1,
     bmi2:  function(){
        return this.Mass/this.Heigth;
    }
};

if(firstPerson.bmi()>secomdPerson.bmi2()){
    console.log(firstPerson.Fullname+' has the largest BMI');
}
else{
    console.log(secomdPerson.Fullname +' has the largest BMI');

}