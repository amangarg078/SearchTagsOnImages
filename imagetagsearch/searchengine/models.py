from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tags(models.Model):
    def __unicode__(self):
        return self.tag_name
    id=models.AutoField(primary_key=True,default=1)
    tag_name=models.CharField(max_length=200)
    tag_images=models.TextField()
    def image_list(self):
        return self.tag_images.split(',')
    
class Image(models.Model):
    def __unicode__(self):
        return self.image_name
    id=models.AutoField(primary_key=True, default=1)

    image_name=models.CharField(max_length=200)
    image_tags=models.TextField()
