# code here
import json

# some dictionaries
p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Pedro", "age":17, "city":"San Paulo"}
p3 = { "name":"Wesley", "age":16, "city":"New York"}
p4 = { "name":"Zach", "age":16, "city":"Toronto"}
p5 = { "name":"David", "age":16, "city":"Seoul"}

# a list of dictionaries
list_of_people = [p1, p2, p3, p4, p5]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
#list_of_people2 = dict_people['people']

for person in dict_people['people']:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()


# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)

for char in json_people:
    print(char, end='+')
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
# INSERT CODE HERE





# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(list_of_people)
# the result is a JSON file:
print("\nJSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
json_dict_people = json.loads(json_people)
for person in json_dict_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()

from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
import aboutdata
from flask_login import (current_user, LoginManager, login_user, logout_user, login_required, UserMixin)
import requests
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
db = SQLAlchemy(app)
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(UserID=userid).first()
    user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
    """filter email by userid"""
    email = Emails.query.filter_by(UserID=userid).first()
    if email:
        user_dict['emails'] = email.email_address
    """filter phone number by userid"""
    pn = PhoneNumbers.query.filter_by(UserID=userid).first()
    if pn:
        user_dict['phone_numbers'] = pn.phone_number
    return user_dict


# CRUD update
# user_dict{} expects userid, email, phone_number
def model_update(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    """update email in table from data in form if it exists, insert if not"""
    if Emails.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Emails).filter_by(UserID=userid).update({Emails.email_address: user_dict["email"]})
    else:
        email = Emails(email_address=user_dict["email"], UserID=userid)
        db.session.add(email)
    """update phone number in table from data in form"""
    if PhoneNumbers.query.filter_by(UserID=userid).first() is not None:
        db.session.query(PhoneNumbers).filter_by(UserID=userid).update(
            {PhoneNumbers.phone_number: user_dict["phone_number"]})
    else:
        phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
        db.session.add(phone_number)

    """commit changes to database"""
    db.session.commit()


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    """delete userid rows from emails table"""
    db.session.query(Emails).filter(Emails.UserID == userid).delete()
    """delete userid rows from phone numbers table"""
    db.session.query(PhoneNumbers).filter(PhoneNumbers.UserID == userid).delete()
    """delete userid rows from users table"""
    db.session.query(Users).filter(Users.UserID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # filter email
        email = Emails.query.filter_by(UserID=user.UserID).first()
        if email:
            user_dict['emails'] = email.email_address
        # filter phone number
        pn = PhoneNumbers.query.filter_by(UserID=user.UserID).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        # append to records
        records.append(user_dict)
    return records
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    user = Users(username=user_dict["username"], password=user_dict["password"])
    """add and commit data to user table"""
    db.session.add(user)
    db.session.commit()
    """prepare data for related tables extracting from form and using new UserID """
    userid = db.session.query(func.max(Users.UserID))
    email = Emails(email_address=user_dict["email"], UserID=userid)
    phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
    """email table add and commit"""
    db.session.add(email)
    db.session.commit()
    """phone number table add and commit"""
    db.session.add(phone_number)
    db.session.commit()

@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form"""
        user_dict = {'username': request.form.get("username"), 'password': request.form.get("password"),
                     'email': request.form.get("email"), 'phone_number': request.form.get("phone_number")}
        # model_create expects: username, password, email, phone_number
        model_create(user_dict)
    return redirect(url_for('pythondb_bp.databases'))


# CRUD read, which is filtering table based off of ID
@app.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid
        user_dict = model_read(userid)
        # model_read returns: username, password, email, phone_number
        record = [user_dict]  # placed in list for compatibility with index.html
    return render_template("pythondb/index.html", table=record, menus=menus)


# CRUD update
@app.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("ID"),
            'email': request.form.get("email"),
            'phone_number': request.form.get("phone_number")
        }
        # model_update expects userid, email, phone_number
        model_update(user_dict)
    return redirect(url_for('pythondb_bp.databases'))


# CRUD delete
@app.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        model_delete(userid)
    return redirect(url_for('pythondb_bp.databases'))