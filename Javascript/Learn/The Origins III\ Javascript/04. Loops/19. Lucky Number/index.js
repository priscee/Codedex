const luckyNumber = 7
let guess = Math.floor(Math.random() * 10) + 1;

while (guess != 7) {
  console.log("Nope, it isn't ", guess);
  guess = Math.floor(Math.random() * 10) + 1
}

console.log("My lucky number is 7!");