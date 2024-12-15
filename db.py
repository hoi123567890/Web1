import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():
    db = sqlite3.connect(".database/one.db")
    db.row_factory = sqlite3.Row
    return db

def reveiw(id):
    db = GetDB()
    media = db.execute("SELECT * FROM Review WHERE media_id=?",(id,)).fetchall()
    db.close()
    return media

def load_games_from_db():
    db = GetDB()
    indi_game = db.execute("SELECT * FROM media WHERE game=1").fetchall()
    db.close()
    return indi_game

def load_movie_from_db():
    db = GetDB()
    indi_movie = db.execute("SELECT * FROM media WHERE game=0").fetchall()
    db.close()
    return indi_movie

def load_media_from_db(id):
    db = GetDB()
    media = db.execute("SELECT * FROM media WHERE id=?",(id,)).fetchone()
    db.close()
    return media

def email_veri(email):
    db = GetDB()
    media = db.execute("SELECT * FROM user WHERE email=?",(email,)).fetchone()
    db.close()
    return media

def pass_veri(email,password):
    db = GetDB()
    media = db.execute("SELECT * FROM user WHERE email=?",(email,)).fetchone()
    if check_password_hash(media['password'], password):
        x= db.execute("SELECT * FROM user WHERE email=?",(email,)).fetchone()
        db.close()
        return x['username']
    else:
        return False

def register(email,pa,last, frist,name):
    db = GetDB()
    hash = generate_password_hash(pa)
    try:
        db.execute("INSERT INTO User(username, password, fristname, lastname,email) VALUES(?,?,?,?,?)", (name,hash,frist,last,email,))
        db.commit()
        return True   
    except sqlite3.IntegrityError:
        return "error"
    finally:
        db.close()