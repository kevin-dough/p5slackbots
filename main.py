from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import aboutdata

import requests

data = requests.get("https://api.hypixel.net/player?key=b3c1bb6d-47ec-4134-bb7c-7da1cebd54f6&name=CrazyUdon").json()
data1 = requests.get("https://api.hypixel.net/player?key=ef3afdee-e7d1-4e5c-a711-b96032716a60&name=sea7wa").json()
dbURI = 'sqlite:///users.sqlite3'
username = "CrazyUdon"
teamskywarswins = data["player"]["achievements"]["skywars_wins_team"]
totalbedwarslevel = data["player"]["achievements"]["bedwars_level"]
solobedwarslootbox = data["player"]["achievements"]["bedwars_loot_box"]

username1 = "sea7wa"
teamskywarswins1 = data1["player"]["achievements"]["skywars_wins_team"]
totalbedwarslevel1 = data1["player"]["achievements"]["bedwars_level"]
solobedwarslootbox1 = data1["player"]["achievements"]["bedwars_loot_box"]


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=False, nullable=False)
    bedwarslevel = db.Column(db.String(255), unique=False, nullable=False)
    skywarswins = db.Column(db.String(255), unique=False, nullable=False)
    bedwarslootbox = db.Column(db.String(255), unique=False, nullable=False)
    def __repr__(self):
        return "<User Id: {}>".format(self.id)

    def __init__(self, username, bedwarslevel, skywarswins, bedwarslootbox):
        self.username = username
        self.bedwarslevel = bedwarslevel
        self.skywarswins = skywarswins
        self.bedwarslootbox = bedwarslootbox

# Starting the app routes
# This is the stuff that lets the website redirect to different pages

# This is the first page that comes up when you start the program
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/soundboards")
def soundboards():
    return render_template("selector.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/electronic")
def electronic():
    return render_template("soundboard1.html", blockdatalist=aboutdata.blockdata())

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/database")
def database():

    return render_template("database.html", users=Users.query.all())

@app.route("/about")
def about():
    return render_template("about.html", groupdatalist=aboutdata.groupdata())

@app.route("/egg")
def egg():
    return render_template("easteregg.html")

if __name__ == "__main__":
    db.create_all()
    Users.query.delete()
    u1 = Users(username=username, bedwarslevel=totalbedwarslevel, skywarswins=teamskywarswins, bedwarslootbox=solobedwarslootbox)
    u2 = Users(username=username1, bedwarslevel=totalbedwarslevel1, skywarswins=teamskywarswins1, bedwarslootbox=solobedwarslootbox1)
    db.session.add_all([u1, u2])
    db.session.commit()
    app.run(debug=True, host='127.0.0.1')
