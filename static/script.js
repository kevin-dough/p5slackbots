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

img = document.getElementById("blueKey");

        function resizeImg() {
            img.style.width = "30%";
            img.style.height = "auto";
            img.style.transition = "width 0.5s ease";
        }

        function resetImg() {
            img.style.width = "40%";
            img.style.height = "auto";
            img.style.transition = "width 0.5s ease";
        }