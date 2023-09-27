from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Task

class TaskModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test task
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
        Test that a task can be created with the specified fields.
        """
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.complete, False)
        self.assertEqual(self.task.frequency, 'Daily')
        self.assertEqual(self.task.importance, 'A')
        self.assertEqual(self.task.completed, 'InComplete')
        self.assertEqual(self.task.user, self.user)

    def test_task_str_representation(self):
        """
        Test the __str__ method of the Task model.
        """
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_default_due_date(self):
        """
        Test that the default due date is set to the current date.
        """
        from django.utils import timezone
        self.assertEqual(self.task.due, timezone.now().date())

    def test_task_ordering(self):
        """
        Test the ordering of tasks by 'complete' field.
        """
        # Create another task with a different complete value
        task2 = Task.objects.create(
            user=self.user,
            title='Another Task',
            complete=True,
            frequency='Daily',
            importance='A',
            completed='InComplete'
        )
        
    def tearDown(self):
        # Clean up test data if needed
        self.task.delete()
        self.user.delete()


