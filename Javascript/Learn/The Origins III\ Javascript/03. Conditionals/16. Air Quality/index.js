let aqi = 148

if (aqi > 0 && aqi < 51) {
  console.log("Good");
} else if (aqi > 50 && aqi < 101) {
  console.log("Moderate");
} else if (aqi > 100 && aqi < 151) {
  console.log("Unhealthy (Sensitive Groups)");
} else if (aqi > 150 && aqi < 201) {
  console.log("Unhealthy");
} else if (aqi > 200 && aqi < 301) {
  console.log("Very Unhealthy");
} else {
  console.log("Hazardous");
}