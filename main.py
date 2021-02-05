from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import aboutdata
from flask_login import (current_user, LoginManager, login_user, logout_user, login_required, UserMixin)
import requests
from werkzeug.security import generate_password_hash, check_password_hash

data = requests.get("https://api.hypixel.net/player?key=b3c1bb6d-47ec-4134-bb7c-7da1cebd54f6&name=CrazyUdon").json()
data1 = requests.get("https://api.hypixel.net/player?key=ef3afdee-e7d1-4e5c-a711-b96032716a60&name=sea7wa").json()
dbURI = 'sqlite:///authuser.sqlite3'
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
app.config['SECRET_KEY'] = 'my_secret_key'
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

#starting logins
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



class AuthUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(500))
    email = db.Column(db.String(50))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {"name": self.name,
                "email": self.email}

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    return AuthUser.query.get(user_id)
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

@app.route("/hypixelapi")
def hypixelapi():
    return render_template("hypixelapi.html")

@app.route("/electronic")
def electronic():
    return render_template("soundboard1.html", blockdatalist=aboutdata.blockdata())

@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/demorestricted")
@login_required
def demorestricted():
    return render_template("demorestricted.html")

@app.route("/database")
def database():

    return render_template("database.html", users=Users.query.all())

@app.route("/about")
def about():
    return render_template("about.html", groupdatalist=aboutdata.groupdata())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    print(request.form.get("username"))
    if request.form.get("username") != "" and request.form.get("username") is not None:
        this_user = AuthUser.query.filter_by(name=request.form.get("username")).first()
        print ('1')
        if this_user and AuthUser.check_password(this_user, password=request.form.get("password")):
            login_user(this_user)
            print ('2')
            return redirect('/')
    print ('3')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template("signup.html")

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

    AuthUser.query.delete()
    user1 = AuthUser("John", generate_password_hash('password1', method='sha256'), "John@gmail.com")
    user2 = AuthUser("Paul", generate_password_hash('password2', method="sha256"), "Paul@gmail.com")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    app.run(debug=True, host='127.0.0.1')
