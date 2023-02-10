from django.test import TestCase
from django.utils import timezone

from task.forms import TaskForm
from task.models import Task
from django.conf import settings


# Define a test case class
class TaskTestCase(TestCase):

    def test_model(self):
        # Create a task instance
        task = Task.objects.create(title={settings.LANGUAGE_CODE: 'Test Task'})

        # Check if the task instance has been created successfully
        self.assertTrue(Task.objects.filter(id=task.id).exists())

        # Check if the task title is returned correctly
        self.assertEqual(str(task), 'Test Task')

        # Check if the task is_done field is set to False by default
        self.assertFalse(task.is_done)

        # Check if the task created field has the correct value
        self.assertLessEqual(task.created, timezone.now())

        # Check if the task updated field has the correct value
        self.assertLessEqual(task.updated, timezone.now())

    def test_form(self):
        # Create a task instance
        task = Task.objects.create(title={settings.LANGUAGE_CODE: 'Test Task'})

        # Check if the form data is correctly saved
        form = TaskForm(data={'is_done': True, f'title_{settings.LANGUAGE_CODE}': 'Test Task2'}, instance=task)
        self.assertTrue(form.is_valid())
        task = form.save()
        self.assertEqual(task.title, {settings.LANGUAGE_CODE: 'Test Task2', 'fr': '', 'hi': ''})
        self.assertTrue(task.is_done)
