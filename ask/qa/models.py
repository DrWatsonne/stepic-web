from django.db import models
from django.contrib.auth.models import User

class MyUser(User):
    class Meta:
        proxy = True

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(MyUser)
    likes = models.ManyToManyField(MyUser)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(MyUser)


# Create your models here.
