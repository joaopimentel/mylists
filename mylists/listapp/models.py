from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from mailfetcher.models import MailBox


class Category(models.Model):
    name = models.CharField(max_length=63)
    tag = models.SlugField(unique=True)

    def __unicode__(self):
        return unicode(self.name)


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=2000)
    comment = models.CharField(max_length=2000,
                               default='',
                               blank=True,
                               null=True)
    date_added = models.DateTimeField(default=datetime.now)
    category = models.ManyToManyField(Category, blank=True)
    user = models.ForeignKey(User)
    read = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.title)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    mailbox = models.OneToOneField(MailBox)

    def __unicode__(self):
        return unicode(self.user) + u' profile'
