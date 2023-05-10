from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from random import randint

from sqlalchemy.sql import func, text

with open('flag.txt', 'r') as file:
    flag = file.read()

#flag='flag_{r4vCUVvo0B}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///database.db'
    # 'sqlite:///' + os.path.join(basedir, '/db/db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50),nullable=False)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __repr__(self) -> str:
        return f'<User {self.firstname}>'

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<Product {self.name}>'

with app.app_context():
    db.drop_all()
    db.create_all()
    session = db.session()
    new_user = User(email='test@test.com', password='Password', name='Foo')
    new_user2 = User(email='coolmail@example.com', password=flag, name='Anna Andersson')
    session.add(new_user)
    session.add(new_user2)

    fruit_names = ['Apple', 'Banana', 'Orange', 'Grapefruit', 'Pineapple', 'Mango', 'Watermelon', 'Kiwi', 'Cherry', 'Peach', 'Pear', 'Plum']
    fruits = []
    for i in fruit_names:
        name = i
        price = round(randint(1, 100) + randint(0, 99) / 100, 2)
        stock = randint(1, 100)
        fruit = Fruit(name=name, price=price, stock=stock)
        fruits.append(fruit)

    session.bulk_save_objects(fruits)
    session.commit()

@app.route("/", methods=('GET','POST'))

def index():
    if request.method == 'POST':
        input = request.form['search']
        if input == '':
            return render_template('index.html')

        query = f"SELECT name,price,stock FROM Fruit WHERE name LIKE '%{input}%'"
        try:
            results = session.execute(text(query))
        except Exception as e:
            print(e)
            return render_template('index.html',error="Server error")
        rows = results.fetchall()
        if not rows:
            error = f"There are no products named {input}"
            return render_template('index.html',error=error)

        return render_template('index.html', data=rows)

    return render_template('index.html')
