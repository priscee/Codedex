const car = { 
    model: "Tesla",
    year: "2022",
    color: "pink",
    used: false
  }
  
  if (car.used) {
    console.log("I'm looking for a " + car.year + " " + car.model + " that is used.")
  } else {
    console.log("I'm looking for a " + car.year + " " + car.model + " that is new.")
  }