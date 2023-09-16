from flask import Blueprint

camera = Blueprint('camera', __name__, url_prefix='/v0/cameras')