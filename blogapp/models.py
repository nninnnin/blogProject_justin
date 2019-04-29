from django.db import models


class Blog(models.Model):  # class overriding
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):  # method overriding
        return self.title

    def summary(self):
        return self.body[:25]
