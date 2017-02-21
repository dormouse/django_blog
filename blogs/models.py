import datetime
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    create_date = models.DateTimeField('date created')
    modify_date = models.DateTimeField('date modified')
    pub_date = models.DateTimeField('date published')
    # tags
    # category
    # author
    summary = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    item = models.ForeignKey(Entry, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content
