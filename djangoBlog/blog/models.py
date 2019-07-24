from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=255)
    pub_date=models.DateTimeField('date published')

    def was_published_recently(self):
        return(self.pub_date>=timezone.now()-datetime.timedelta(days=1))

    def __str__(self):
        return(self.question_text)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return(self.choice_text)

class Post(models.Model):
    user=models.ForeignKey('User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    imgTitle=models.URLField()

class User(models.Model):
    nickName=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    headImage=models.URLField()

