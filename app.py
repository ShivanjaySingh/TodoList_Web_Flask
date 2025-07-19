from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///SitaRamtodo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route('/', methods = ["GET", "POST"])
def JaySitaRam():
    if request.method == 'POST':
        print("POST")
        print("Title: ", request.form['title'])
        print("Description: ", request.form['desc'])

        # Storing value of form in the variable
        title = request.form['title']
        desc = request.form['desc']
   
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo = allTodo)
    

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno = sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/update/<int:sno>', methods = ['POST', 'GET'])
def Update(sno):
    if(request.method == 'POST'):
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno = sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html', todo = todo)

@app.route('/show')
def Show():
   allTodo = Todo.query.all()
   print(allTodo)
   return 'Jay Sita Ram'

@app.route('/products')
def Products():
    return "Jay Sita Ram This is a product Page"

# create DataBase Tables
with app.app_context():
    db.create_all()
    

if __name__ == "__main__":
    app.run(debug=True)


'''
To run this app You need to activate the virtual environment

Thats how we can activate the virtual environment
".\env\scripts\activate.ps1"

and now to run the app, Runt the commmand
"python .\app.py"

To use database install flask-sqlalchemy
"pip install flask-sqlalchemy"
it is a ORM used to make changes in database using or through Python

If I want database file then run these commands in terminal
"python"
"from app import db"
"db.create_all()"  # Iske baad 1 "todo.db" name ki file create ho jayegi

with app.app_context():
    db.create_all()
'''