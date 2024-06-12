function relativityTheory(mass) {
    const speedOfLight = 299792458;
  
    const energy = mass * (speedOfLight ** 2);
  
    return energy;
  }
  
  console.log(relativityTheory(20));
  console.log(relativityTheory(30));
  console.log(relativityTheory(55));