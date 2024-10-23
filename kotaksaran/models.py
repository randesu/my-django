from django.db import models

# Create your models here.
class kotakSaran(models.Model):
    IdSaran = models.AutoField(primary_key=True)
    IsiSaran = models.CharField()


    class Meta:
        db_table = 'kotaksaran'