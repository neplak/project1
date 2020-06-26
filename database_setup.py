import sys
# for database configuration
import sqlalchemy as db

# for model defining
from sqlalchemy.ext.declarative import declarative_base

# for relationship between tables
from sqlalchemy.orm import relationship


# creation of declarative_base instance
Base = declarative_base()

# classes definition
class User(Base):
    __tablename__ ='user'

    id=db.Column(db.Integer,primary_key=True)
    nick=db.Column(db.String(),unique=True)
    fullName=db.Column(db.String(),unique=True)
    salt=db.Column(db.LargeBinary())
    key=db.Column(db.LargeBinary())

class Author(Base):
    __tablename__ ='author'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(),unique=True,nullable=False)
    books=relationship('Book',backref='author')

class Book(Base):
    __tablename__ ='book'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(),nullable=False)
    isbn=db.Column(db.String(),nullable=False)
    year=db.Column(db.DateTime,nullable=False)
    author_id=db.Column(db.Integer,db.ForeignKey(Author.id),nullable=False)
# instance of create_engine

class Comments(Base):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    book_id=db.Column(db.Integer,db.ForeignKey(Book.id),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey(User.id),nullable=False)
    contents=db.Column(db.String(),nullable=False)

engine = db.create_engine('postgresql+psycopg2://books:bNcO9ypR@192.168.1.120:5432/books')

def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__=='__main__':
    main()
