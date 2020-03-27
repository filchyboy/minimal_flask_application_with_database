'''
Base code for application
'''
# import flask module
from flask import Flask, render_template


def create_app():
# initiate application
    app = Flask(__name__)
    
    @app.route('/')
    def root():
        return render_template("home.html")
    return app