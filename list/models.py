from django.db import models
from django.utils import timezone

class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    deadline_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def complete(self):
        self.completed_date = timezone.now()
        self.completed = True
        self.save()

    def __str__(self):
        return self.title