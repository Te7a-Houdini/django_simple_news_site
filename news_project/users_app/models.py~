from __future__ import unicode_literals
from django.db import models

# Create your models here.
class category(models.Model):
	category_name = models.CharField(max_length=100)
	def __str__(self):
                return self.category_name
	class Meta:
		ordering = ('category_name',)

class post(models.Model):

	post_category= models.ForeignKey(category)
	title = models.CharField(max_length=30,null=False )
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
        image = models.ImageField(upload_to='documents/%Y/%m/%d')
        def __str__(self):
                return self.title
	
	class Meta:
		ordering = ["-created"]
		
class tag(models.Model):
	tag_name = models.CharField(max_length=100)
	posts = models.ManyToManyField(post,through='posts_tags')#specify intermediate class in many to many relationship
	def __str__(self):
                return self.tag_name

        class Meta:
		ordering = ('tag_name',)
		
class posts_tags(models.Model):#intermediate class between posts and tags
    post_id = models.ForeignKey(post)
    tag_id = models.ForeignKey(tag)





