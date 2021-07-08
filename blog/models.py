
from django.db import models

# Create your models here.
# database ----> Excel workbook
# Models in Django ----> Table ---------> Sheet

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    short_desc = models.CharField(max_length=550, default="")
    auther = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField( blank=True)

    def __str__(self):
        return self.title + 'by' + self.auther