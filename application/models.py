from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class AQ(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    utc = DB.Column(DB.String(128))
    value = DB.Column(DB.Integer)