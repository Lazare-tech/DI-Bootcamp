//Is palindrome?
let y,i,taille;
function isPalindrome(chaine){
  taille=chaine.length;
  console.log(taille);
  for(y=0;y<=taille;y++){
        if(chaine[y]!==chaine[taille-1-y])
          {
            return "it is not palindrome";
          }
  }
  return "it is  palindrom";
}
isPalindrome("kayak");