from django.contrib import admin
from listapp import models

admin.site.register(models.Category)
admin.site.register(models.Link)
admin.site.register(models.UserProfile)
