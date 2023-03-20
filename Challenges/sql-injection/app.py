from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///database.db'
    # 'sqlite:///' + os.path.join(basedir, '/db/db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())

    def __repr__(self) -> str:
        return f'<User {self.firstname}>'

with app.app_context():
    db.drop_all()
    db.create_all()
    new_user = User(email='test@test.com', firstname='Foo',lastname='Bar',bio='A test user')
    db.session.add(new_user)
    db.session.commit()
    print("testing")



@app.route("/")
def hello_world():
    users = User.query.all()
    print(users[0].email)
    return f"<p>Hello, World! {users[0].email}</p>"

@app.route('/data')
def render_path():
    foo = str(request.query_string)
    return foo

