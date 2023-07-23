from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    image = models.URLField(max_length=200, null=True)
    pub_date = models.DateTimeField()
    content = models.TextField()

# Comment code:

class Comment(models.Model):
    post = models.ForeignKey('news.NewsStory', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
