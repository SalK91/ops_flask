#import flask
from flask import Flask, redirect, url_for, render_template

# Create application instance - WSGI protocol
app = Flask(__name__)

@app.route('/') # Slash means domain name only - default page
def index():
    return render_template("index.html")


@app.route('/<name>') #<> grabs the value the link
def print_name(name):
    return f'Hello Hello <h1> {name} <h1>'

@app.route("/admin") 
def admin():
    return redirect(url_for("print_name", name="Admin Access not allowed")) # redirected to another page (function name, variable values)

if __name__ == '__main__':
    app.run(debug=True)