from django.db import models


class Chat(models.Model):
    sender = models.CharField(max_length=256)
    receiver = models.CharField(max_length=256)
    msg = models.TextField()
    time = models.DateTimeField()

class Users(models.Model):
    user_id = models.CharField(max_length=256)
    last_visit = models.DateTimeField()