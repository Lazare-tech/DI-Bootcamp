let sentence="The movie is not that bad, I like it";
let wordNot=sentence.indexOf("not");
let  wordBad=sentence.indexOf("bad");
console.log(wordNot);
if(wordBad>wordNot){
    console.log("The movie is good,i like it");
}
else{
    console.log(sentence);
}

