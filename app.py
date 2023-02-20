import json

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from tables.cameras import Camera
from tables.users import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:huihui27@localhost/snapshots'
db=SQLAlchemy(app)



class Snapshot(db.Model):
  __tablename__='snapshots'
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

  snapshot=Snapshot(time,event,trigger)
  db.session.add(snapshot)
  db.session.commit()

  #debugging
  snapshotResult=db.session.execute(db.select(Snapshot)).scalars()
  
  for result in snapshotResult:
    print(result.event)

  return render_template('success.html', data=event)


@app.route('/snapshots')
def snapshots():
  return json.dumps(db.session.execute(db.select(Snapshot)).scalars())



app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:huihui27@localhost/cameras'
app3 = Flask(__name__)
app3.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:huihui27@localhost/cameras'


db__cameras=SQLAlchemy(app2)
db__users=SQLAlchemy(app3)

class Camera(db__cameras.Model):
  __tablename__='cameras'
  id=db.Column(db__cameras.Integer,primary_key=True)
  location=db.Column(db__cameras.String(40))

  def __init__(self,location):
    self.location = location


@app.route('/cameras')
def cameras():
  return db.session.execute(db__cameras.select(Camera)).scalars()

@app.route('/users')
def users():
  return 1



if __name__ == '__main__': 
  app.run(debug=True)