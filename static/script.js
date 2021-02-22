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

/*
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
*/

var character = document.getElementById("character");
var block = document.getElementById("block");
var counter=0;
function jump(){
    if(character.classList == "animate"){return}
    character.classList.add("animate");
    setTimeout(function(){
        character.classList.remove("animate");
    },300);
}
var checkDead = setInterval(function() {
    let characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    let blockLeft = parseInt(window.getComputedStyle(block).getPropertyValue("left"));
    if(blockLeft<20 && blockLeft>-20 && characterTop>=130){
        block.style.animation = "none";
        alert("Game Over. score: "+Math.floor(counter/100));
        counter=0;
        block.style.animation = "block 1s infinite linear";
    }else{
        counter++;
        document.getElementById("scoreSpan").innerHTML = Math.floor(counter/100);
    }
}
