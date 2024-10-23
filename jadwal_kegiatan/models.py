from django.db import models

# Create your models here.
class jadwalKegiatan(models.Model):
    IdKegiatan = models.AutoField(primary_key=True)
    TanggalKegiatan = models.DateField()
    NamaKegiatan = models.CharField()

    
    class Meta:
        db_table = 'jadwalKegiatan'