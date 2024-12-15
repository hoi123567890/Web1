from flask import Flask, flash, render_template, request, session, redirect, url_for
import time
from db import *
x=0
app = Flask(__name__)
app.secret_key = "y_u_looking"

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def Add():
    if session.get('username') == None:
        return redirect("/")

@app.route('/email', methods=['GET', 'POST'])
def email_route():
    if request.method == 'POST':
        variable = request.form['email_address']
        veri=email_veri(variable)
        if veri is None:
            return redirect(url_for('register_route', email=variable))
        else:
            return redirect(url_for('login_route', email=variable))
    else:
        return render_template("email.html")

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    email = request.args.get('email')
    print(email)
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        password = request.form['password']
        veri= pass_veri(email,password)
        if veri == False:
            flash('Invalid password.', 'error')
            return render_template("password.html")  
        else:
            x = veri
            return redirect("/")
    else:
        return render_template("password.html") 
@app.route('/register', methods=['GET', 'POST'])
def register_route():
    email = request.args.get('email')
    if request.method == 'POST':
        con_password= request.form['con_password']
        password = request.form['password']
        first_name = request.form['frist_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']

        veri=email_veri(email)
        if veri is None:
           if con_password == password:
               veri = register(email, password, last_name, first_name, username)
               if veri is True:
                    flash('Registration successful!', 'success')
                    return redirect(url_for('home'))
               else:
                    flash('Choose another username.', 'error')
                    return render_template("register.html") 
           else:
                flash('Passwords do not match.', 'error')
                return render_template("register.html") 
        else:
            return redirect(url_for('login_route', email=email))
    else:
        return render_template("register.html")  

@app.route('/game')
def game():
    Games = load_games_from_db()
    return render_template("game.html", title="Game",g=Games)

@app.route('/game/<id>')
def show_game(id):
    game = load_media_from_db(id)
    review = reveiw(id)
    if not game:
        return "Not found", 404
    else:
        return render_template("item.html", game=game, review=review)

@app.route('/movie')
def movie():
    Movies = load_movie_from_db()
    return render_template("game.html", tittle="Moive",g=Movies)

@app.route('/movie/<id>')
def show_movie():
    movie = load_media_from_db(id)
    if not movie:
        return "Not found", 404
    else:
        return render_template("item.html", game=movie)

if __name__ == "__main__":
    app.run(debug=True, port=5000)