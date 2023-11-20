from flask import Flask
from .config import Config
from flask_restful import Api
from dotenv import load_dotenv
from flasgger import Swagger
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# LOAD ENVIRONMENT
load_dotenv()

# INIT FLASK APP -- START
app = Flask(__name__)
app.config.from_object(Config)
# INIT FLASK APP -- END

# INIT DB AND MIGRATIONS -- START
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate
api = Api(app)
# INIT DB AND MIGRATIONS -- START

# IMPORT URLS -- START
from .resources.task import TaskAPI
from .resources.task_list import TaskListAPI

api.add_resource(TaskListAPI, '/tasks')
api.add_resource(TaskAPI, '/tasks/<int:id>')
# IMPORT URLS -- END

# INIT SWAGGER -- START
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
# INIT SWAGGER -- END
