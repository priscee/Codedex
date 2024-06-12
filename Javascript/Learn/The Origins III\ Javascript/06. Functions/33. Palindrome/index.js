function isPalindrome(word) {
    let wordReverse = "";
  
    let lowerCase = word.toLowerCase();
  
    for (let i = lowerCase.length - 1; i >= 0; i--) {
      wordReverse += lowerCase[i];
    }
    return wordReverse == lowerCase;
  }
  
  console.log(isPalindrome("Racecar"));
  console.log(isPalindrome("madam"));
  console.log(isPalindrome("moonlight"));
  console.log(isPalindrome("Aviary"));