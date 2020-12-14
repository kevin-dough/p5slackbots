from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Starting the app routes
# This is the stuff that lets the website redirect to different pages

# This is the first page that comes up when you start the program
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

# This is the
@app.route("/support")
def support():
    return render_template("support.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)