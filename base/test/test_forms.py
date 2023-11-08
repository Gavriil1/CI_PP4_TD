from django.test import TestCase
from base.forms import PostForm


class TestTaskForm(TestCase):

    def test_task_form_valid_data(self):
        """
        Checks if form is valid when correct data is provided.
        """
        form = PostForm(data={
            'title': 'Test Title',
            'description': 'Test Description',
            'completed': 'Completed',
            'frequency': 'Daily',
            'importance': 'A',
            'due': '2023-09-07',
        })

        self.assertTrue(form.is_valid())

    def test_task_form_blank_data(self):
        """
        Checks if form is invalid where correct data is not provided
        """
        form = PostForm(data={})

        self.assertFalse(form.is_valid())

    def test_task_form_invalid_due_date(self):
        """
        Checks if form is invalid when wrong date is provided.
        """
        form = PostForm(data={
            'title': 'Test Title',
            'description': 'Test Description',
            'completed': 'Completed',
            'frequency': 'Daily',
            'importance': 'A',
            'due': 'invalid date',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('due', form.errors)
