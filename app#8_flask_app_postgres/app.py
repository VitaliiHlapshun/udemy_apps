# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sending_mail import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://odoo13:odoo13@localhost/app#8'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


class Profile(db.Model):
    __tablename__ = "profile"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True)
    last_name = db.Column(db.String(120), unique=True)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height_)).scalar()
            average_height = round(average_height, 1)
            participants_count = db.session.query(Data.height_).count()
            send_email(email, height, average_height, participants_count)
            print(average_height)
            return render_template("success.html")
        return render_template("index.html", text="Seems like you've got already one")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
