# minimal_flask_application_with_database
A minimal flask application with database

FLASK_APP=application flask run
from application import APP
from application.models import *

DB.create_all()
utc = AQ(utc='2020', id=1)
value = AQ(value=3, id=2)
DB.session.add(utc)
DB.session.add(value)
DB.session.commit()