from flask_restful import Resource, reqparse
from flasgger import swag_from
from ..models import Task
from .. import db


class TaskListAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help="Title cannot be blank!")
    parser.add_argument('description')
    parser.add_argument('status')

    @swag_from('docs/get_list.yml', methods=['GET'])
    def get(self):
        tasks = Task.query.all()
        return [task.serialize() for task in tasks]

    @swag_from('docs/post.yml', methods=['POST'])
    def post(self):
        data = TaskListAPI.parser.parse_args()
        task = Task(title=data['title'], description=data['description'], status=data['status'])
        db.session.add(task)
        db.session.commit()
        return task.serialize(), 201
