const dnaPieces = ["A", "C", "G", "T"];

const myDNA = [];

for (let i = 0; i < 24; i++) {
  const firstpiece = Math.floor(Math.random () * dnaPieces.length);
  const secondpiece = Math.floor(Math.random () * dnaPieces.length);
  const thirdpiece = Math.floor(Math.random () * dnaPieces.length);

  myDNA.push(dnaPieces[firstpiece]+ dnaPieces[secondpiece] + dnaPieces[thirdpiece]);
}

console.log(myDNA)