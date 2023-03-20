import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///database.db'
    # 'sqlite:///' + os.path.join(basedir, '/db/db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


print(app.config)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self) -> str:
        return f'<User {self.firstname}>'

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


@app.route("/")
def hello_world():
    new_user = User(email='test@test.com')
    db.session.add(new_user)
    db.session.commit()
    return "<p>Hello, World!</p>"

@app.route('/data')
def render_path():
    foo = str(request.query_string)
    return foo
