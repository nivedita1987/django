from django.db import models
class Registermod(models.Model):
    fn=models.CharField(max_length=50)
    ea=models.EmailField()
    pa=models.CharField(max_length=50)
    

# Create your models here.
