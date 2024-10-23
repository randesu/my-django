from django.db import models

# Create your models here.
class rumahJentik(models.Model):
    IdRumah = models.AutoField(primary_key=True)
    NomorRumah = models.CharField(max_length=64)
    KepalaRumah = models.CharField(max_length=64)
    AlamatRumah =  models.CharField(max_length=255)
    JumlahKontainer = models.CharField()
    KontainerJentik = models.CharField()

    # def __str__(self):
    #     return      


    class Meta:
        db_table = 'rumahJentik'