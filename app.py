from flask import Flask,Blueprint, render_template, request, jsonify,redirect, url_for

app = Flask(__name__)
@app.route ('/')
def home():
    return render_template("index.html")

@app.route ('/game')
def game():
    return render_template("game.html")

@app.route ('/game/<id>')
def show_game():
    game = load_games_from_db()
    if not game:
        return "Not found", 404
    else:
        return render_template("item.html", game=game)

@app.route ('/movie')
def movie():
    return render_template("movie.html")

@app.route ('/movie/<id>')
def show_moive():
    moive = load_movie_from_db()
    if not movie:
        return "Not found", 404
    else:
        return render_template("item.html", game=movie)

@app.route("/email/<id>" meathod=["post"])
def email(id):
    email=request.form
    return jsonify.data

if __name__ == "__main__":
    app.run(debug=True, port=8000)