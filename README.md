# slackboard
#### Created by the P5 Slackbots -  Kevin Do, Abhijay Deevi, and Kian Kishimoto
project still in beta development, test

### Description:
slackboard is a sleek and clean online soundboard which allows you to create that sick beat you've been dreaming about.
This interactive soundboard allows users to produce their own beats with our sounds or even with their own 
sounds. Users can create their own soundboards or find custom-made soundboards on our public library, compiled by users from all around the globe. 
Users will also be able to record and upload their recordings to our public gallery so other users can see their masterpieces.

These soundboards aren't the typical click on the screen to make a noise, but they are interactive. From button animations and being able to play sounds with the click of the key, you will be able to produce your own custom beats at ease.

Runtime Link: http://slackboard.cf/home

### Website Navigation: 

Main Slackboards: 
1. As soon as you enter into the soundboard world of slackboard.cf, you will notice a "how to" page. The website gives you some basic instructions on how to use the slackboard. You can test these rules out with the 4 square soundboard on the left of the screen with the sounds, "bruh," "cola," "rickroll," and "yo." Once you are done looking at the rules, press the purple "let's go" button to enter into the main slackboards. 
2. Once you press that button, you enter a different screen with a small scrollbar at the top. Press that and you will see three options. "memeboard" is a soundboard that allows you to play sounds of different well known memes like the ali-a intro. "beatboard" allows you to play different beats and make a really nice peice. It's like being a DJ and making cool tunes. "pickboard" is under construction at the moment, but it will become something amazing. Once you choose your soundboard, press the music note button that is to the right of the scrollbar. 
3. Wow! A full soundboard, that corresponds to your keyboard, shows up! Go ahead and use your mouse to press the buttons and listen to the music! Make different stories with the memeboard or making soundtracks with the beatboard. It's all up to you!

Other Features: 
1. At the top of the page, you will notice a navigation bar. The soundboard button will just redirect you the soundboard page that we talked about earlier. You can follow the steps above to use those soundboards. 
2. The second option on the navigation bar is the about us page. This talks about the creators of the slackboard. Place your mouse over each person to create a nice animation that slides in information about us and links to our socials. 
3. The next option on the navigation bar is profile. If you already have an account with us, this allows you to login. If you are new, there is a sign up page right below the login page. Press the link that says "sign up." Here you can create a new account (don't actually use your real passwords because this website is not secure). Once you sign up, you can go back to login page and sign in. 
4. Finally, at the end of the navigation bar is logout button, which just logs you out of your account. 
5. Secret: There's actually an easter egg in this website. Try to find it! You'll find the creator's linkedin profiles. Also, you can play our music game that is still under construction. It is called musicjump, a game just like the dinosaur game! You have a score and animation all ready to go! Also, you can check out our Hypixel statistics through our API database table. 

### Technicals
Abhijay mainly focused on front end (HTML, CSS, javascript, jinja). Kian mainly focused on backend (python, HTML). Kevin mainly focused on deploying (Raspberry Pi, working with Linux terminal). The technicals we incorporated are: setting up a functioning website (Flask), CRUD ([inspiration](http://nighthawkcoders.cf/pythondb/#BE-MODELCRUD)), databases (SQLAlchemy), API, connecting the website to the internet with a public domain ([inspiration](https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/README.md)), user accounts and authentication ([inspiration](https://docs.google.com/document/d/1F6iYBj5xJ8ZWCtkDqlF_-skWM-Xuut-BqT5eRNPhnOE/edit)), and JSON lists and dictionaries ([inspiration](https://www.w3schools.com/python/python_dictionaries.asp)). We set up a functioning website and connected it to the internet with a public [domain](http://slackboard.cf/home) on the Raspberry Pi. We used CRUD in the [signup funcction](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L152), databases to [hold API data](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L27) as well as [website users for login/logout functions](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L49), and we used [JSON lists and dictionaries for the API](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L8) and for [displaying the content of the Easter Egg page](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/aboutdata.py). 

### Week of 2/16-18
#### [Current Assignments](https://github.com/kevin-dough/p5slackbots/projects/1#column-11960379)
- Kevin: Jinja Loop to print soundboard - Completed // Add new sounds to soundboard - Completed
    - [Memeboard Data](https://github.com/kevin-dough/p5slackbots/blob/main/memeboarddata.py)
    - [Memeboard Jinja Loops](https://github.com/kevin-dough/p5slackbots/blob/main/templates/memeboard.html)
    - [Tutorial Page Jinja Loops](https://github.com/kevin-dough/p5slackbots/blob/2bbac02c2f6281628ace68c401070172ed00e694/templates/index.html#L10-L24)
- Abhijay: Add more sounds to the soundboard - In Progress
    - [Sounds Folder](https://github.com/kevin-dough/p5slackbots/tree/main/static/sounds)
- Kian: Sign Up Feature - In Progress
    - [Sign Up Page](https://github.com/kevin-dough/p5slackbots/blob/main/templates/signup.html)
    - [Sign Up Code](https://github.com/kevin-dough/p5slackbots/blob/main/main.py) *update link*
#### [Future Assignments](https://github.com/kevin-dough/p5slackbots/projects/1#column-11996245)
- [College Board Project Requirements Plans](https://docs.google.com/document/d/1TvRvscxNA3tDbC-ohQ4H73_G4iKtURiGGdrjs4D2uBY/edit)


### Who am I?
Click [here](https://github.com/kevin-dough/p5slackbots/blob/795680c0c610b8a48df186b52c80701008b970f1/templates/easteregg.html#L8-L49) to see the code for the "Who am I?" portion of our code!

### Easter Egg!
You gave up already? Aww, c'mon! At least try to find the easter egg without coming here for the answer. Fine, I guess I have to give it to you.
I'm only going to give you the link. If you really want to find out how to get to the page, you're gonna have to work for it.
[Easter Egg](http://slackboard.cf/egg)

#### [Week 7 Tickets](https://github.com/kevin-dough/p5slackbots/projects/1#column-11996245)

### Week of 1/11 Goals
- Kian: Database Creation and Implementation
- Kevin: Soundboard Selection Menu and Basic Layout + Footer w/ Light/Dark Switch
- Abhijay: Light/Dark Switch Functionality

### Week of 1/11 Writeup
#### Kevin:

Scrum Master Score: 20/20

Self-Reflection: 
This week I finished both of my goals, which were to create selection menu to switch between soundboards and a footer, where the dark/light mode switch would be. I was able to work with Abhijay to create what we have so far with the dark/light mode switch. The selection menu is not functional yet, but next week I will create soundboard layouts and then use POST to switch between them. I did a bit of JavaScript and got a bit more comfortable with it when doing the light/dark mode switch.

#### Abhijay:

Scrum Master Score: 20/20

Scrum Master Note: Abhijay stepped up his animation work by using more JavaScript along with his CSS code.

Self-Reflection: 
Moving into JavaScript is a little harder for me, so I am trying to use different websites to try and learn all those things. I was able to use some JavaScript to make the light mode to night mode switch on every page, which is a pretty good accomplishment. I still need to learn how to apply it to the navigation bar, which I will complete next week. I need to get better at JavaScript to finish this part and also make all the nice animations.

#### Kian:

Scrum Master Score: 19/20

Scrum Master Note: Kian put a lot of effort into putting together our database but was unable to produce have his work shown in our repository because of issues with the virtual machine. 

Self-Reflection: 
This week I unfortunately wasn't able to finish my goal of completely integrating the database into the website because it was actually a lot more complicated than I thought. I don't have a Pi, which makes it pretty difficult to do, and I also had a lot of problems actually testing a local database with a virtual machine. Next week, I'll be able to integrate the database and get it functioning as well as get the API to retrieve the data from the online sound libraries.


### Resources
For each sound on the sound boards, we will pull data from public sound libraries online, for example https://freesound.org/, https://www.epidemicsound.com/sound-effects/, and https://www.zapsplat.com/. Each sound file has its own url which we'll be able to utilize to link to each button for the soundboard. However, for some of the soundboards we'll make custom sounds by recording and uploading files to use locally. 

### Delivery Plans/Objectives:  
Midterm: First Fully Functionable Soundboard 
- The soundboard will be able to be clicked and be able to play sounds. The soundboard will have clicking animations and users will be able to use their keyboard to click the onscreen buttons.

N@TM: Multiple Soundboards
- We will have multiple themed soundboards for the user to use such as electronic, acoustic drums, etc. Users will be able to record themselves playing the soundboard and play it to hear again.

Collegeboard: Final Touch Ups and 0 Bugs
- Users will be able to upload their recordings to our public library for others to play and listen to it. The library will store their songs and also store their username so listeners can know who the producer of the song is.


### Database Implementation
Users
- names of users that upload to public library

Soundboards/Sounds
- custom soundboards made by people which can be shared on a public library
- our default soundboards and their sounds

Recordings
- recordings can be created and shared to the public library

### Mockup Images

Home Page:
<p>
<img src="https://media.discordapp.net/attachments/744422103788552192/788653409645101066/unknown.png" height=40% width=40%>
</p>

About Page: 
<p>
<img src="https://media.discordapp.net/attachments/744422103788552192/788653979671199754/unknown.png" height=40% width=40%>
</p>

### Table of Collaborators
|      Name      | Github Username |
|:--------------:|:---------------:|
|    Kevin Do    |   kevin-dough   |
|  Abhijay Deevi |     Dubshott    |
| Kian Kishimoto |     Uhpachee    |
 
 

### Important Project Links:
[Project Plan](https://docs.google.com/document/d/1AE2wDFp38JuWuyR5VViy-U6sAXsbcRyoU44dgAqBC0o/edit)

[Scrum Board](https://github.com/kevin-dough/p5slackbots/projects/1)
