from statistics import mode
from django.db import models

# Create your models here.

class ModelForAddress(models.Model):
    SrNo = models.CharField(max_length=25)
    NametoAdd = models.CharField(max_length=250)
    phonetoadd = models.CharField(max_length=250)
    addresstoadd = models.CharField(max_length=250)
