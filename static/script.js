const sounds = ["bruh", "cola", "rickroll", "yo"];

sounds.forEach((sound) => {
  playbruh = () => {
    document.getElementById('bruh').play()
    }

  playcola = () => {
    document.getElementById('cola').play()
    }
  playrickroll = () => {
    document.getElementById('rickroll').play()
    }
  playyo = () => {
    document.getElementById('yo').play()
    }



  const btn = document.createElement("button");
  btn.classList.add("btn");

  btn.innerText = sound;

  btn.addEventListener("click", () => {
    stopSongs();

    document.getElementById(sound).play();
  });

  document.getElementById("buttons").appendChild(btn);
});

function playAudio(url) {
  new Audio(url).play();
}

