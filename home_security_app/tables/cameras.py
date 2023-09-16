from home_security_app.extensions import db 

class Camera(db.Model):
  __bind_key__ = "cameras"
  __tablename__='cameras'
  id=db.Column(db.Integer, primary_key=True)
  location=db.Column(db.String(40))

  def __init__(self,location):
    self.location = location