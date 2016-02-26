from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import post,tag,category,posts_tags


# Register your models here.



from models import  *



admin.site.register(post)

admin.site.register(tag)

admin.site.register(category)

class inline(admin.StackedInline):
   #extra=3
   model=posts_tags

    
class customize(admin.ModelAdmin):
   inlines=[inline]
   search_fields = ['title']
   list_filter = ['content']
   list_display = ('title','post_category','image')
   
  
   
admin.site.register(category)
admin.site.register(post,customize)
admin.site.register(tag)
fields = ( 'image_tag', )
readonly_fields = ('image_tag',)


