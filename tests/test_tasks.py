import unittest
from app import app, db
from app.models import Task
from tests.test_config import TestConfig

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestConfig)
        self.app = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_empty_tasks(self):
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_post_task(self):
        response = self.app.post('/tasks', json={'title': 'New Task', 'description': 'Test Description', 'status': 'pending'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Task', response.json['title'])

    def test_get_task(self):
        response = self.app.post('/tasks', json={'title': 'Specific Task', 'description': 'Test', 'status': 'pending'})
        task_id = response.json['id']
        response = self.app.get(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['title'], 'Specific Task')

# More tests can be added for update and delete functionalities

if __name__ == '__main__':
    unittest.main()
