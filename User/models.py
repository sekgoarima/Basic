from django.db import models

# Create your models here.
class detail(models.Model):
    id=models.IntegerField(primary_key=True)
    name =models.CharField(max_length=64)
    surname =models.CharField(max_length=64)
    idnumber =models.IntegerField()
    email =models.EmailField(max_length=254)
    cellnumber =models.IntegerField()

class modules(models.Model):
    module =models.CharField(max_length=64)
    




