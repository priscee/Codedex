const pig = {
    name: "Babe",
    type: "pig",
    age: 5,
    makeSound() {
      console.log(pig.name + " is a " + pig.age + " year old " + pig.type + " that goes oink!")
    }
  }
  pig.makeSound();
  
  const sheep = {
    name: "Shaun",
    type: "sheep",
    age: 87,
    makeSound() {
      console.log(sheep.name + " is a " + sheep.age + " year old " + sheep.type + " that goes baaah!")
    }
  }
  sheep.makeSound();
  
  const dog = {
    name: "Clifford",
    type: "dog",
    age: 50,
    makeSound() {
      console.log(dog.name + " is a " + dog.age + " year old " + dog.type + " that goes woof!")
    }
  }
  dog.makeSound();