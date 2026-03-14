from flask import Flask

app = Flask(__name__)

@app.route("/username/gurjeet")
def say_bye():
    return "<p>Welcome, Gurjeet!</p>"