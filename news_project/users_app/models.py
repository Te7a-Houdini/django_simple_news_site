from __future__ import unicode_literals
from django.db import models


''' New Imports '''

#used for ckeditor app so that it can upload files especialy for image
from ckeditor_uploader.fields import RichTextUploadingField




class tag(models.Model):

    tag_name = models.CharField(max_length=100)

    class Meta:

        ordering = ('tag_name',)

    #override to show the name of tag
    def __str__(self):
        return self.tag_name;


class category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('category_name',)

    def __str__(self):
        return self.category_name;


class post(models.Model):

    post_category= models.ForeignKey(category)

    title= models.CharField(max_length=30,null=False,default="Title" )

    content = RichTextUploadingField()

    created = models.DateTimeField(auto_now_add=True)

    #blank to accept the empty tag
    tag = models.ManyToManyField(tag ,blank=True)


    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title;







