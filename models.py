import config
from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    __tablename__ ='user'

    id=db.Column(db.Integer,primary_key=True)
    nick=db.Column(db.String(),unique=True)
    fullName=db.Column(db.String(),unique=True)
    salt=db.Column(db.String(32))
    key=db.Column(db.String())

class Author(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),unique=True,nullable=False)
    books=db.relationship('Book',backref='author')

class Book(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(),nullable=False)
    isbn=db.Column(db.String(),nullable=False)
    year=db.Column(db.DateTime,nullable=False)
    author_id=db.Column(db.Integer,db.ForeignKey(author.id),nullable=False)


def main():
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    pass

if __name__=='__main__':
    main()
