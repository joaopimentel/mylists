from django.db import models


class MailBox(models.Model):
    """Info to access into receiver mail boxes to grab data."""
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
