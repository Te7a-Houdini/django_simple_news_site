from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import post,tag,category


# Register your models here.



from models import  *



admin.site.register(post)

admin.site.register(tag)

admin.site.register(category)
