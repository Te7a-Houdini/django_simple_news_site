from django.contrib import admin

# Register your models here.

from models import  *



admin.site.register(post)

admin.site.register(tag)

admin.site.register(category)