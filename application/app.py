'''
Base code for application
'''
# import flask module
from flask import Flask, render_template
from .models import DB

def create_app():
# initiate application
    app = Flask(__name__)
    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_db.sqlite3'
    # point to database within app
    DB.init_app(app)
    
    @app.route('/')
    def root():
        return render_template("home.html")
    return app