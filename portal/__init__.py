from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')

login_manager = LoginManager(app)

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import portal.views
