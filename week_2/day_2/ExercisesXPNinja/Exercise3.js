let code=prompt("Entrer un mot");
let reg=/[^aeiouy]/g;
let result=code.match(reg);

console.log(result);