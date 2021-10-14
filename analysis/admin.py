from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Batsman)
admin.site.register(models.Bowler)
admin.site.register(models.Stadium)
