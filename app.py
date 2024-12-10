from flask import Flask,Blueprint, render_template, request, jsonify,redirect, url_for

app = Flask(__name__)
@app.route ('/')
def home():
    return render_template("index.html")

@app.route ('/game')
def games():
    return render_template("games.html")

@app.route ('/movie')
def moive():
    return render_template("moives.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)