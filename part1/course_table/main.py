# Таблица сообщений
# Создайте модель Course по таблице course:
# +----+-------------------+---------+-------+-------+
# | id |       title       | subject | price | weeks |
# +----+-------------------+---------+-------+-------+
# | 1  | Введение в Python |  Python | 11000 |  3.5  |
# | 2  |  Пишем на Spring  |   Java  | 15000 |  8.0  |
# | 3  |   Игры на Python  |  Python | 13500 |  5.0  |
# | 4  |    Игры на Java   |   Java  |  9000 |  4.5  |
# +----+-------------------+---------+-------+-------+
#
#
import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO определите модель здесь
class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    subject = db.Column(db.Text)
    price = db.Column(db.Integer)
    weeks = db.Column(db.Float)


db.create_all()

city_rym = Course(id=1, title="Введение в Python", subject="Python", price="2873000", weeks=3.5)
city_milan = Course(id=2, title="Пишем на Spring", subject="Java", price="1333000", weeks=8.0)
city_venice = Course(id=3, title="Игры на Python", subject="Python", price="265000", weeks=5.0)
city_venic = Course(id=4, title="Игры на Java ", subject="Java", price="265000", weeks=4.5)

italian = [city_rym, city_milan, city_venice, city_venic]

db.session.add_all(italian)
db.session.commit()

# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла
db.create_all()
session = db.session()
cursor = session.execute(f"SELECT * from {Course.__tablename__}").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
