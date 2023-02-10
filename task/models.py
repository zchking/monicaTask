from django.db import models

# Create your models here.
from django.conf import settings

from django.db import models


class Task(models.Model):
    """
    This model has a JSONField title for storing the translated titles, as well as created and updated fields for
    storing the creation and last modification timestamps, respectively.
    This model has an additional BooleanField `is_done` to indicate whether the task has been completed or not.
    """
    title = models.JSONField("Task_Title", default=dict)
    is_done = models.BooleanField("Is Done", default=False)
    created = models.DateTimeField("Created", auto_now_add=True)
    updated = models.DateTimeField("Updated", auto_now=True)

    def __str__(self):
        return self.title.get(settings.LANGUAGE_CODE, 'Title')
