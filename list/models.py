from django.db import models
from django.utils import timezone

class Item(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    COLORS = (
        ('rgb(255, 138, 128)','red'),
        ('rgb(128, 216, 255)','blue'),
        ('rgb(255, 255, 141)','yellow'),
        ('rgb(255, 209, 128)','orange'),
        ('rgb(204, 255, 144)','green'),
        ('rgb(207, 216, 220)','grey'),
        ('rgb(167, 255, 235)','teal'),
    )
    color = models.CharField(max_length=20,choices=COLORS)
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True,null=True)
    image = models.URLField(blank=True,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    archived_date = models.DateTimeField(blank=True, null=True)
    archived = models.BooleanField(default=False)

    def archive(self):
        self.archived_date = timezone.now()
        self.archived = True
        self.save()

    def dearchive(self):
        self.archived_date = None
        self.archived = False
        self.save()

    def __str__(self):
        return self.title

