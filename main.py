from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Home"
    return render_template("index.html",title=title)

@app.route('/about')
def about():
    title = "About"
    return render_template("about.html",title=title)

@app.route('/team')
def team():
    title = "Team"
    return render_template("team.html",title=title)

@app.route('/contact')
def contact():
    title = "Contact"
    return render_template("contact.html",title=title)

app.run(host='0.0.0.0', port=81)
