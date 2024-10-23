from django.db import models

# Create your models here.
class anggotaPosyandu(models.Model):
    IdAnggota = models.AutoField(primary_key=True)
    NamaAnggota = models.CharField(max_length=64)

    def __str__(self):
        return self.NamaAnggota

    class Meta:
        db_table = 'anggotaPosyandu'