import csv
import datetime as dt
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
# импортируем классы Book и Base из файла database_setup.py
from database_setup import User, Author, Book, Base

engine = db.create_engine('postgresql+psycopg2://books:bNcO9ypR@192.168.1.120:5432/books')
# Свяжим engine с метаданными класса Base,
# чтобы декларативы могли получить доступ через экземпляр DBSession
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# Экземпляр DBSession() отвечает за все обращения к базе данных
# и представляет «промежуточную зону» для всех объектов,
# загруженных в объект сессии базы данных.
session = DBSession()


def selectOrCreateAuthor(aname):

    ret=session.query(Author).filter_by(name=aname).first()
    if ret is None:
        a=Author(name=aname)
        session.add(a)
        session.commit()
        id=a.id
        return id
    else:
        return ret.id

def selectOrCreateBook(title,isbn,year,author_name):
    au_id=selectOrCreateAuthor(author_name)
    b=Book(title=title,isbn=isbn,year=year,author_id=au_id)
    ret=session.query(Book).filter_by(isbn=isbn).first()
    if ret is None:
        session.add(b)
        session.commit()
        return b.id
    else:
        return ret.id

def loadData(fname):
    with open(fname,newline='') as fin:
        reader=csv.DictReader(fin)
        counter=0
        for row in reader:
            y=dt.datetime(int(row['year']),1,1)
            r=selectOrCreateBook(row['title'],row['isbn'],y,row['author'])
            if r:
                counter+=1
    return counter


def main():
    c=loadData('books.csv')
    print(c)

if __name__=='__main__':
    main()
