from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate  # Import Flask-Migrate
from dotenv import load_dotenv
from .config import Config
from flasgger import Swagger


load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "version": "1.0.0",
            "title": "Task Management API",
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/"
}

Swagger(app, config=swagger_config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
api = Api(app)

from .resources.task import Task
from .resources.task_list import TaskList

api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/tasks/<int:id>')
