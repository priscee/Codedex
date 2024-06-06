const player = 2
const computer = Math.floor(Math.random() * 3)

console.log("Player picked: ", player);
console.log("Computer picked: ", computer);

/*
0 == rock
1 == scissors
2 == paper
*/

if (player == 0) { /*player choose rock*/
  if (computer == 0) {
    console.log("Draw");
  } else if (computer == 1) {
    console.log("Player won!");
  } else if (computer == 2) {
    console.log("Computer won!");
  } else {
  console.log("Error");
  } 
} else if (player == 1) { /*player choose scissors*/
    if (computer == 0) {
      console.log("Computer won!");
    } else if (computer == 1) {
      console.log("Draw");
    } else if (computer == 2) {
      console.log("Player won!");
    } else {
    console.log("Error");
    }
} else if (player == 2) { /*player choose paper*/
    if (computer == 0) {
      console.log("Player won!");
    } else if (computer == 1) {
      console.log("Computer won!");
    } else if (computer == 2) {
      console.log("Draw");
    } else {
    console.log("Error");
  }
} else {
  console.log("Error");
}