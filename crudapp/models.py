from django.db import models

# Create your models here.

class Usercrud(models.Model) :
    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    branch = models.CharField(max_length=20) 
    image = models.FileField(upload_to='uploads/',max_length=250,null=True,default=None)

    class Meta:
        db_table = 'Usercrud'

    def delete(self, *args, **kwargs):
        # Delete the image file when the Usercrud object is deleted
        self.image.delete()
        super().delete(*args, **kwargs)