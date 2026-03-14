from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    static_image_url = "static/flask.png"
    return render_template("index.html", static_image_url=static_image_url)

if __name__ == "__main__":
    app.run(debug=True)