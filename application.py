import os
import hashlib

from flask import Flask, session, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config
from database_setup import User, Author, Book

app = Flask(__name__,template_folder='my_templates',static_folder="my_scripts")
app.config.from_object(config.Config)
# Check for environment variable
# if not os.getenv("DATABASE_URL"):
    # raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
db_session = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register/",methods=['post','get'])
def register():
    msg=""
    if request.method=='POST':
        nick=request.form.get('nickname')
        fullname=request.form.get('fullname')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        salt=os.urandom(32)
        key=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),salt,100000)
        # print(f"{type(password.encode('UTF-8'))} {type(salt)} {type(key)}")
        u=User(nick=nick,fullName=fullname,salt=salt,key=key)
        query=db_session.query(User).filter_by(nick=nick)
        res=query.first()
        if res:
            msg='User already exists'
        else:
            db_session.add(u)
            db_session.commit()
            msg=f'User {nick} succesfully added'
    return render_template('register.html',message=msg)

@app.route("/login/",methods=['post','get'])
def login():
    msg=""
    if request.method=='POST':
        nick=request.form.get('username')
        password=request.form.get('password')
        query=db_session.query(User).filter_by(nick=nick)
        res=query.first()
        if not res:
            msg='Wrong user name or password'
        else:
            salt=res.salt
            print(f'{salt} {type(salt)} {password}')
            new_key=hashlib.pbkdf2_hmac('sha256',password.encode('UTF-8'),salt,100000)
            if new_key==res.key:
                # password is corerect
                msg='Welcome!'
                db_session["user_id"]=res.id
            else:
                msg='Wrong user name or password'
    return render_template('login.html',message=msg)
