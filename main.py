from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import aboutdata

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
db = SQLAlchemy(app)
records = []
class items(db.Model):
    id = db.Column('item_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    price = db.Column(db.Float(200))
def init(self, id, name, type, price, image):
    self.name = name
    self.id = id
    self.type = type
    self.price = price

db.create_all()
"""
@app.route("/database")
def shopowner():
    form = ItemForm()
    "Validate the forms"

    if form.validate_on_submit():  # adding in all
        new_item = items(type=form.type.data, name=form.name.data, price=form.price.data, image = form.image.data)
        db.session.add(new_item)
        db.session.commit()
        user_dict = {'id': new_item.id, 'name': new_item.name, 'type': new_item.type, 'price': new_item.price}
        records.append(user_dict)
        return render_template("database.html", form=form, table=records)
"""

records = []#int the list

@app.route("/database",methods=['GET','POST'])
def shopowner():
    #form = ItemForm()#collecting all information from form
    "Validate the forms"
    #collecitng ingormation from the form
    if request.method == 'POST':#forms will always post
        form = request.form
        name = form['name']
        password = form['password']
        gender = form['gender']
        email = form['email']
        phonenumber = form['phonenumber']

        new_item = items(name=name, password=password,gender=gender, email = email, phonenumber = phonenumber )
        db.session.add(new_item) #penciing into db
        db.session.commit()#commitng to data

        user_dict = {'name': name, 'password': password, 'gender': gender, 'email': email, 'phonenumber': phonenumber}

        records.append(user_dict)
        return render_template("database.html", table=records)


def list_map():  # mapping the front end to the backend, put in the function so we don't have to copy and paste this all the time
    item = items.query.all()
    for item in item:
        user_dict = {'id': item.id, 'name': item.name, 'type': item.type, 'price': item.price}
        records.append(user_dict)

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

@app.route("/electronic")
def electronic():
    return render_template("soundboard1.html", blockdatalist=aboutdata.blockdata())

@app.route("/support")
def support():
    return render_template("support.html")

"""@app.route("/database")
def database():
    return render_template("database.html")"""

@app.route("/about")
def about():
    return render_template("about.html", groupdatalist=aboutdata.groupdata())

@app.route("/egg")
def egg():
    return render_template("easteregg.html")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
