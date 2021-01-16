# slackboard
#### Created by the P5 Slackbots -  Kevin Do, Abhijay Deevi, and Kian Kishimoto
project still in beta development


### Description:
slackboard is a sleek and clean online soundboard which allows you to create that sick beat you've been dreaming about.
This interactive soundboard allows users to produce their own beats with our sounds or even with their own 
sounds. Users can create their own soundboards or find custom-made soundboards on our public library, compiled by users from all around the globe. 
Users will also be able to record and upload their recordings to our public gallery so other users can see their masterpieces.

These soundboards aren't the typical click on the screen to make a noise, but they are interactive. From button animations and being able to play sounds with the click of the key, you will be able to produce your own custom beats at ease.

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
