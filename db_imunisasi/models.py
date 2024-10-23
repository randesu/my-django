from django.db import models

# Create your models here.
class imunisasi(models.Model):
    IdAnak = models.AutoField(primary_key=True)
    NamaAnak = models.CharField(max_length=64)
    VaksinKe = models.CharField()
    JenisVaksin = models.CharField()
    
    # def __str__(self):
    #     return self.NamaBayi


    class Meta:
        db_table = 'imunisasi'