from django.db import models

# Create your models here.

class Togri_soz(models.Model):
  soz=models.CharField(max_length=100)
  def __str__(self) -> str:
    return self.soz
  
class Xato_soz(models.Model):
  xato=models.CharField(max_length=50)
  soz=models.ForeignKey(Togri_soz,on_delete=models.CASCADE)
  
  def __str__(self) -> str:
    return self.xato