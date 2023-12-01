from django.db import models

class Tour(models.Model):
  origin: models.CharField(max_length=64)
  destination: models.CharField(max_length=64)
  days: models.IntegerField()
  price: models.IntegerField()
