const memeArray = [
    "https://i.imgur.com/bSi4xLb.png",
    "https://i.imgur.com/6y0G7N0.png",
    "https://i.imgur.com/LXnRao1.png",
    "https://i.imgur.com/Qqoxh1N.png"
  ];
  
  const captionArray = [
    "Stealing hearts and plotting chaos.",
    "Dream big, plot bigger.",
    "Slaying... but like, literally.",
    "Jet-setting and trouble-making.",
  ];
  
  const randomMeme = document.getElementById("random-meme");
  const randomCaption = document.getElementById("random-caption");
  const generatorButton = document.getElementById("generator-button");
  
  generatorButton.addEventListener("click", function() {
    const randomMemeIndex = Math.floor(Math.random() * memeArray.length);
    const randomCaptionIndex = Math.floor(Math.random() * captionArray.length);
  
    randomMeme.src = memeArray[randomMemeIndex];
    randomCaption.innerText = captionArray[randomCaptionIndex];
  })