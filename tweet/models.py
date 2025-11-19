from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='Untitled')
    text=models.TextField(max_length=1000)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    
    likes = models.ManyToManyField(User, related_name='tweet_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='tweet_dislikes', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def __str__(self):
        return f"{self.user.username} - {self.title}"