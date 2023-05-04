from flask import Flask, render_template, g, request, url_for, redirect
import container_manager

import docker
# from flask_sqlalchemy import SQLAlchemy
# from random import randint

# from sqlalchemy.sql import func, text

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] =\
    # 'sqlite:///database.db'
    # # 'sqlite:///' + os.path.join(basedir, '/db/db.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # email = db.Column(db.String(50),unique=True, nullable=False)
    # password = db.Column(db.String(50),nullable=False)
    # name = db.Column(db.String(50), nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    # def __repr__(self) -> str:
        # return f'<User {self.firstname}>'

# with app.app_context():
    # db.drop_all()
    # db.create_all()
    # session = db.session()
    # new_user = User(email='test@test.com', password='Password', name='Foo')
    # new_user2 = User(email='coolmail@example.com', password=flag, name='Anna Andersson')
    # session.add(new_user)
    # session.add(new_user2)

    # fruit_names = ['Apple', 'Banana', 'Orange', 'Grapefruit', 'Pineapple', 'Mango', 'Watermelon', 'Kiwi', 'Cherry', 'Peach', 'Pear', 'Plum']
    # fruits = []
    # for i in fruit_names:
        # name = i
        # price = round(randint(1, 100) + randint(0, 99) / 100, 2)
        # stock = randint(1, 100)
        # fruit = Fruit(name=name, price=price, stock=stock)
        # fruits.append(fruit)

    # session.bulk_save_objects(fruits)
    # session.commit()

client = docker.from_env()

temp_name="sqli-challenge"

status = {
    "msg" : "",
    "on" : False,
}

@app.route("/<int:challenge_id>")
def index(challenge_id):
    print(challenge_id)
    data = {}
    res = container_manager.check_status(temp_name)
    if res["on"]:
        data["on"] = res["on"]
    print("@@@check@@@")
    print(res)
    return render_template('index.html', challenge_id=challenge_id, status=data)

@app.route("/<int:challenge_id>/container_start", methods=['POST'])
def start(challenge_id):
    res = container_manager.start()
    print("@@@start@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))

@app.route("/<int:challenge_id>/container_stop", methods=['POST'])
def container_stop(challenge_id):
    res = container_manager.stop()
    print("@@@stop@@@")
    print(res)

    return redirect(url_for('index', challenge_id=challenge_id))
