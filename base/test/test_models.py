from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Task


class TaskModelTestCase(TestCase):
    def setUp(self):
        """
        Creates a test user.
        Test that a task can be created with the specified fields.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='This is a test task.',
            complete=False,
            frequency='Daily',
            importance='A',
            completed='InComplete'
        )

    def test_task_creation(self):
        """
        Test that the task was created with correct entries.
        """
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.complete, False)
        self.assertEqual(self.task.frequency, 'Daily')
        self.assertEqual(self.task.importance, 'A')
        self.assertEqual(self.task.completed, 'InComplete')
        self.assertEqual(self.task.user, self.user)

    def tearDown(self):
        """
        Test that the task was created with correct entries.
        """
        self.task.delete()
        self.user.delete()
