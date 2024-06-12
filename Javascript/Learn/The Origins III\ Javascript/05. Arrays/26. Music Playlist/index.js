const musicPlaylist = [
    "Tom Sawyer",
    "Sabotage",
    "I Wanna Dance With Somebody",
    "Don't Speak",
    "Bulls On Parade",
    "Thriller",
    "The Breaks",
    "Brick",
    "Aeroplane Over the Sea",
    "Tubthumping"
  ];
  
  const firstElement = musicPlaylist.shift();
  console.log(musicPlaylist);
  
  const lastElement = musicPlaylist.pop();
  console.log(musicPlaylist);
  
  musicPlaylist.push("Cruel Summer");
  console.log(musicPlaylist);
  
  musicPlaylist.unshift("Houdini", "Espresso");
  console.log(musicPlaylist);