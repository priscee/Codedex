const question = "Are you good?"

const randomNumber = Math.floor(Math.random() * 9) + 1

let answer = ""

console.log("Question: ", question);
console.log("Answer: ", answer);

if (randomNumber == 1) {
  console.log("Yes - definitely");
} else if (randomNumber == 2) {
  console.log("It is decidedly so.");
} else if (randomNumber == 3) {
  console.log("Without a doubt.");
} else if (randomNumber == 4) {
  console.log("Reply hazy, try again.");
} else if (randomNumber == 5) {
  console.log("Ask again later.");
} else if (randomNumber == 6) {
  console.log("Better not tell you now.");
} else if (randomNumber == 7) {
  console.log("My sources say no.");
} else if (randomNumber == 8) {
  console.log("Outlook not so good.");
} else if (randomNumber == 9) {
  console.log("Very doubtful.");
} else {
  console.log("Error");
}
