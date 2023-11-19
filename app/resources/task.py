from flask_restful import Resource, reqparse
from flasgger import swag_from
from ..models import Task
from .. import db


class Task(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', required=True, help="Title cannot be blank!")
    parser.add_argument('description')
    parser.add_argument('status')

    @swag_from('docs/get.yml', methods=['GET'])
    def get(self, id):
        task = Task.query.get(id)
        if task:
            return task.serialize()
        return {'message': 'Task not found'}, 404

    @swag_from('docs/update.yml', methods=['PUT'])
    def put(self, id):
        data = Task.parser.parse_args()
        task = Task.query.get(id)

        if task:
            task.title = data['title']
            task.description = data['description']
            task.status = data['status']
            db.session.commit()
            return task.serialize()
        return {'message': 'Task not found'}, 404

    @swag_from('docs/delete.yml', methods=['DELETE'])
    def delete(self, id):
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task deleted'}
        return {'message': 'Task not found'}, 404
