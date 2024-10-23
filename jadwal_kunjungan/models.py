from django.db import models

# Create your models here.
class jadwalKunjungan(models.Model):
    IdKunjungan = models.AutoField(primary_key=True)
    TanggalKunjungan = models.DateField()
    NamaKunjungan = models.CharField()
    DeskripsiKunjungan = models.CharField()

    class Meta:
        db_table = 'jadwalKunjungan'