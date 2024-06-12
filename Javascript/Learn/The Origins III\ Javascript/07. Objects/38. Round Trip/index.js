// Depart Trip Ticket
const departTripTicket = {
  name: "Brandon",
  from: "Pittsburgh, PA",
  to: "Augsburg, Germany",
  businessClass: false,
  upgrade() {
    if (departTripTicket.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      departTripTicket.businessClass = true;
      console.log("You have been upgraded to business class!");
    }
  }
}

departTripTicket.leaveTime = 24;
departTripTicket.arriveTime = 13;
departTripTicket.flightTime = function() {
  let flightTime = departTripTicket.arriveTime - departTripTicket.leaveTime;
  if (flightTime < 0) {
    flightTime = flightTime * -1;
  }
  console.log(flightTime + " hours")
}

departTripTicket.upgrade();
departTripTicket.flightTime();

// Return Trip Ticket
const returnTripTicket = {
  name: "Brandon",
  from: "Augsburg, Germany",
  to: "Pittsburgh, PA",
  businessClass: true,
  upgrade() {
    if (returnTripTicket.businessClass) {
      console.log("Your ticket is already business class!");
    } else {
      returnTripTicket.businessClass = true;
      console.log("You have been upgraded to business class!");
    }
  }
}

returnTripTicket.leaveTime = 14;
returnTripTicket.arriveTime = 3;
returnTripTicket.flightTime = function() {
  let flightTime = returnTripTicket.arriveTime - returnTripTicket.leaveTime;
  if (flightTime < 0) {
    flightTime = flightTime * -1;
  }
  console.log(flightTime + " hours")
}

returnTripTicket.upgrade();
returnTripTicket.flightTime();