import datetime

from django.db import models

from user.models import User


# Create your models here.
class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    partner_nickname = models.CharField(max_length=24, default="default_nickname")  # 상대방의 닉네임
    start_date = models.DateField(default=datetime.date.today)  # 연애 시작일

    def __str__(self):
        return f"Content by {self.user.id}"


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    emotion = models.CharField(max_length=20)
    privacy = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    #wordcloud = models.FileField(upload_to='wordclouds/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
