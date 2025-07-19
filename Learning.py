from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///learning.db'
app.config('SQLALCHEMY_TRACK_MODIFICATION') = False
db = SQLAlchemy(app)





from flask import flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')

app.config('SQLALCHEMY_DATABSE_URI') = 'SQLITE:///SITARAM.db'
app.config('SQLALCHEMY_TRACK_MODIFICATION') = False

db = SQLAlchemy(app)





from flask import flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")
app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///sitaram.db'

db = SQLAlchemy(app)

class SitaRam:
    rno = db.column(db.Integer(200), primary_key = True)
    name = db.column(db.String(100), nullable = False)
    std = db.cloumn(db.Integer(100), nullable = False)
    grade = db.column(db.String(10), nullable = False)
    contact = db.column(db.Integer(11), nullable = False)

    def __reper__(self):
        return f"{self.rno} - {self.name}"
    
@app.route('/')
def addStudentDetails():
    return render_template('index.html', )


with app.app_context():
    db.create_all()
