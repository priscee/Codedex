const myNumber = 40;

let binary = "";

/* for loop */
for (let i = myNumber; i >= 1; i = Math.floor(i/2)) {
  if (i % 2 == 0) {
    binary = "0" + binary
  } else {
    binary = "1" + binary;
  }
}

console.log(binary)

/* while loop */
let i = myNumber;

while (i >= 1) {
  if (i % 2 == 0) {
    binary = "0" + binary
  } else {
    binary = "1" + binary
  }
  i = Math.floor(i / 2);
}

console.log(binary)