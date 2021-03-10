# slackboard
#### Created by the P5 Slackbots -  Kevin Do, Abhijay Deevi, and Kian Kishimoto
project still in beta development

### Description:
slackboard is a sleek and clean online soundboard which allows you to create that sick beat you've been dreaming about.
This interactive soundboard allows users to produce their own beats with our available library of 70+ sounds! 

Future Features: Users will also be able to record and upload their recordings to our public gallery so other users can see their masterpieces. Users will also be able to upload their own sounds for their custom-made soundboards.

These soundboards aren't the typical click on the screen to make a noise, but they are interactive. From button animations and being able to play sounds with the click of the key (future feature), you will be able to produce your own custom beats at ease.

## Project Links
### Runtime Link: http://slackboard.cf/
- View our project in real time!
### Commercial: https://youtu.be/zx5zcgnR35g
- See our brief overview and teaser for the project!
### Easter Egg: http://slackboard.cf/egg
- You gave up already? Aww, c'mon! At least try to find the easter egg without coming here for the answer. Fine, I guess I have to give it to you. I'm only going to give you the link. If you really want to find out how to get to the page, you're gonna have to work for it.
### Project Plan: [plan document](https://docs.google.com/document/d/1AE2wDFp38JuWuyR5VViy-U6sAXsbcRyoU44dgAqBC0o/edit)
- See our initial goals and plans for the project.
### Scrum Board: https://github.com/kevin-dough/p5slackbots/projects/1
- Here, you can see our assigned and completed tasks.

### Website Navigation: 
Main Slackboards:
1. As soon as you enter into the soundboard world of slackboard.cf, you will notice a "how to" page. The website gives you some basic instructions on how to use the slackboard. You can test these rules out with the 4 square soundboard on the left of the screen with the sounds, "bruh," "cola," "rickroll," and "yo." Once you are done looking at the rules, press the purple "let's go" button to enter into the main slackboards. 
2. Once you press that button, you enter a different screen with a small dropdown menu at the top. Press that and you will see two options. "memeboard" is a soundboard that allows you to play sounds of different well known memes like the ali-a intro. "beatboard" allows you to play different sounds that you would hear on your typical electronic music. Once you choose your soundboard, press the music note button that is to the right of the scrollbar. 
3. A full soundboard that corresponds to your keyboard shows up! Go ahead and use your mouse to press the buttons and listen to the music! Make different stories with the memeboard or soundtracks with the beatboard. It's all up to you!

Other Features: 
1. At the top of the page, you will notice a navigation bar. The soundboard button will just redirect you the soundboard page that was mentioned earlier. You can follow the steps above to use those soundboards. 
2. The second option on the navigation bar is the about us page, which displays the creators of the slackboard. Place your mouse over each person to view wmore information about each person.
3. The next option on the navigation bar is profile. If you already have an account with us, this allows you to login. If you are new, there is a sign up page right below the login page. Press the link that says "sign up." Here you can create a new account (don't actually use your real passwords because this website is not secure). Once you sign up, you can go back to login page and sign in. 
4. Finally, at the end of the navigation bar is logout button, which just logs you out of your account. 
5. Secret: There's actually an easter egg in this website. Try to find it!

### Frontend
- consistent project theme

<img src=https://user-images.githubusercontent.com/54718041/110583588-c641bc00-8122-11eb-8fce-1b5107718e7a.png height="50%" width="50%">

- button click animations on soundboard

<img src=https://user-images.githubusercontent.com/54718041/110583546-b1fdbf00-8122-11eb-82da-4e24831c19ce.png height="40%" width="40%">





### Backend
- setting up a functioning website (Flask)
     - connected to the internet with a public [domain](http://slackboard.cf/home) on the Raspberry Pi
- CRUD ([inspiration](http://nighthawkcoders.cf/pythondb/#BE-MODELCRUD))
     - [signup funcction](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L152)
     - databases to [hold API data](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L27)
     - [website users for login/logout functions](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L49)
- databases (SQLAlchemy)
     - [displaying the content of the Easter Egg page](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/aboutdata.py)
- connecting the website to the internet with a public domain ([inspiration](https://github.com/nighthawkcoders/flask-idea-homesite/blob/master/README.md))
- user accounts and authentication ([inspiration](https://docs.google.com/document/d/1F6iYBj5xJ8ZWCtkDqlF_-skWM-Xuut-BqT5eRNPhnOE/edit))
- JSON lists and dictionaries ([inspiration](https://www.w3schools.com/python/python_dictionaries.asp)
     - [used in the API](https://github.com/kevin-dough/p5slackbots/blob/37bd13d2c72f70d2fa1dfa34f0f2875d7246d0a0/main.py#L8)
- Jinja templates
     - [base header HTML file](https://github.com/kevin-dough/p5slackbots/blob/2956a9366568541b7e7fa9761d11771c9efded2d/templates/base.html#L63-L88)
     - [dislaying of the soundboards](https://github.com/kevin-dough/p5slackbots/blob/2956a9366568541b7e7fa9761d11771c9efded2d/templates/beatboard.html#L8-L22)
- POST
     - [selector menu](https://github.com/kevin-dough/p5slackbots/blob/2956a9366568541b7e7fa9761d11771c9efded2d/templates/selector.html#L5-L18)
     - take the user input and open up the selected soundboard: [code](https://github.com/kevin-dough/p5slackbots/blob/2956a9366568541b7e7fa9761d11771c9efded2d/main.py#L98-L104)
<img src=https://user-images.githubusercontent.com/54718041/110583876-35b7ab80-8123-11eb-8eec-67feef239099.png />


### Technicals
#### Kevin (Scrum Master)
- role: front end & deployment
     - HTML, CSS, RPi, Python Flask, Jinja, ISP DNS
- who am i in computer science?
     - I can build a Python/Flask web server, use Jinja templates, and efficiently develop frontends in HTML, CSS, and Bootstrap.
     - I have done DevOps on Linux, where I set up a Python/Flask server using Gunicorn & Nginx.
     - I can create my own domain using Internet Service Provider DNS records.
#### Abhijay (Scrumling)
- role: front end & animations
     - CSS and JS
- who am i in computer science?
     - I am a professional coder that has learned many different languages such as C, Objective-C, Python, HTML, CSS, and JavaScript.
     - I am working to become a master at each language.
#### Kian (Scrumling)
- role: backend & databases
     - HTML and Python
- who am i in computer science?
     - I can create SQL databases, use API, and code the backend of websites and applications.
     - I am comfortable with working with Linux and with various coding languages, such as HTML, CSS, JavaScript, Python, and Bash.

# First Project Plans

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
 
