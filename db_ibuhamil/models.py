from django.db import models

# Create your models here.
class ibuHamil(models.Model):
    IdIbu = models.AutoField(primary_key=True)
    NamaIbu = models.CharField(max_length=64)
    UmurKehamilan = models.CharField(max_length=64, default=0)
    
    # def __str__(self):
    #     return self.NamaBayi


    class Meta:
        db_table = 'ibuhamil'