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


let response = fetch("https://api.hypixel.net/player?key=b3c1bb6d-47ec-4134-bb7c-7da1cebd54f6&name=CrazyUdon")
print response["player"]["stats"]["SkyWars"]["coins"]

.then(res => res.json())
.then(data => console.log(data))



// api url
const api_url = "https://api.hypixel.net/player?key=b3c1bb6d-47ec-4134-bb7c-7da1cebd54f6&name=CrazyUdon";

// Defining async function
async function getapi(url) {

    // Storing response
    const response = await fetch(url);

    // Storing data in form of JSON
    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
// Calling that async function
getapi(api_url);

// Function to hide the loader
function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
// Function to define innerHTML for HTML table
function show(data) {
    let tab =
        `<tr>
          <th>player</th>
          <th>stats</th>
          <th>SkyWars</th>
          <th>coins</th>
         </tr>`;

    // Loop to access all rows
    for (let r of data.list) {
        tab += `<tr>
    <td>${r.players} </td>
    <td>${r.stats}</td>
    <td>${r.SkyWars}</td>
    <td>${r.coins}</td>
</tr>`;
    }
    // Setting innerHTML as tab variable
    document.getElementById("skywarsWin").innerHTML = tab;
}
