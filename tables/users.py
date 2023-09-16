from extensions import db 

class recognizedFace():
  __bind_key__ = "faces"
  __tablename__='faces'
  id=db.Column(db.Integer, primary_key=True)
  haar_recognition=db.Array(db.Integer)

class User():
  __bind_key__ = "user"
  __tablename__='user'
  id=db.Column(db.Integer, primary_key=True)
  face=db.Column(db.String(40))

  def __init__(self,face):
    self.face = recognizedFace(face)