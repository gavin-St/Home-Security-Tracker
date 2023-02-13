from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:huihui27@localhost/snapshots'

db=SQLAlchemy(app)

class Student(db.Model):
  __tablename__='students'
  id=db.Column(db.Integer,primary_key=True)
  time=db.Column(db.String(40))
  event=db.Column(db.String(40))
  trigger=db.Column(db.String(40))

  def __init__(self,time,event,trigger):
    self.time=time
    self.event=event
    self.trigger=trigger


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
  time=request.form['time']
  event=request.form['event']
  trigger=request.form['trigger']

  student=Student(time,event,trigger)
  db.session.add(student)
  db.session.commit()

  #fetch a certain student2
  studentResult=db.session.query(Student).filter(Student.id==1)
  for result in studentResult:
    print(result.event)

  return render_template('success.html', data=event)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug=True)