from django.db import models

# Create your models here.
class bayi(models.Model):
    IdBayi = models.AutoField(primary_key=True)
    NamaBayi = models.CharField(max_length=64)
    TanggalLahir = models.DateField(null=True)
    
    def __str__(self):
        return self.NamaBayi


    class Meta:
        db_table = 'bayi'