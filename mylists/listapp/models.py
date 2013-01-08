from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=63)

    def __unicode__(self):
        return unicode(self.name)


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.SlugField(max_length=2000)
    comment = models.CharField(max_length=2000,
                               default='',
                               blank=True,
                               null=True)
    date_added = models.DateTimeField(default=datetime.now)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return unicode(self.title)
