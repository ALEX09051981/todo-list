from django.test import TestCase
from django.urls import reverse
from .models import Task, Tag
from datetime import datetime, timedelta

class TaskTests(TestCase):

    def setUp(self):
        self.tag = Tag.objects.create(name="TestTag")
        self.task = Task.objects.create(content="Test Task")

    def test_create_task(self):
        response = self.client.post(reverse('task-add'), {
            'content': 'New Task',
            'deadline': '',
            'is_done': False,
            'tags': [self.tag.id],
        })
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertTrue(Task.objects.filter(content='New Task').exists())

    def test_update_task(self):
        response = self.client.post(reverse('task-update', args=[self.task.id]), {
            'content': 'Updated Task',
            'deadline': '',
            'is_done': False,
            'tags': [],
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, 'Updated Task')

    def test_delete_task(self):
        response = self.client.post(reverse('task-delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_toggle_task(self):
        self.assertFalse(self.task.is_done)
        response = self.client.get(reverse('task-toggle', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
