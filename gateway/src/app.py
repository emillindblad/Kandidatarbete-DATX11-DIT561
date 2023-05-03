from flask import Flask, render_template, g, request

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

status = {
    "msg" : "",
    "on" : False,
}

def check_container_status(container_name):
    try:
        client.containers.get(container_name)
        print("Container started")
        status["on"] = True
    except (docker.errors.NotFound, docker.errors.APIError) as e:
        print(f"Error when starting container {container_name}")
        print(f"Error: {e}")

@app.route("/", methods=('GET','POST'))
def index():
    temp_name="sqli-challenge"
    check_container_status(temp_name)
    print(status)
    return render_template('index.html',status=status)

@app.route("/container_start", methods=['POST'])
def container_start():
    temp_name="sqli-challenge"
    #TODO: probably refactor the container mangement to a different file when using more containers

    dockerfile_path = "../../Challenges/sql-injection"
    image, log_generator = client.images.build(path=dockerfile_path, tag=f"{temp_name}:latest", rm=True)
    print(image.id)

    container = client.containers.run(image.id, ports={5000:8001}, name=temp_name, detach=True)
    #TODO: catch error if port is busy

    container_id = container.id
    status["msg"] = f"Container started with id {container_id}"
    status["on"] = True
    print(status)

    return render_template('index.html',status=status)

@app.route("/container_stop", methods=['POST'])
def container_stop():


    return render_template('index.html',status=status)






