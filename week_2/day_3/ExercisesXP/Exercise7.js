let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let trie=names.sort();
let secret=trie.join(" ");
var secretSociety = secret.match(/\b(\w)/g);

console.log(secretSociety);