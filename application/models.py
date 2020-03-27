from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class AQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    utc = db.Column(db.String(128))
    value = db.Column(db.Integer(128))