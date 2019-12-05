from django.contrib import admin
from api import models


admin.site.register(models.Course)
admin.site.register(models.CourseDetail)
admin.site.register(models.Chapter)
