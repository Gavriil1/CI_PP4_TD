from django.test import TestCase
from base.forms import PostForm

class TestTaskForm(TestCase):

    def test_task_form_valid_data(self):
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
        form = PostForm(data={})

        self.assertFalse(form.is_valid())


    def test_task_form_invalid_due_date(self):
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

    # Add more tests for specific field types or validation rules as needed

# test_task_form_valid_data: This test checks if the form is valid when valid data is provided for all fields.

# test_task_form_blank_data: This test checks if the form is invalid when no data is provided (since some fields are required).

# test_task_form_invalid_due_date: This test checks if the form is invalid when an invalid date is provided for the 'due' field.