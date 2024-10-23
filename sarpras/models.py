from django.db import models

choices = {
    "baik" : "baik",
    "sedang" : "sedang",
    "buruk" : "buruk"
}

# Create your models here.
class sarpras(models.Model):
    IdBarang = models.AutoField(primary_key=True)
    NamaBarang = models.CharField()
    JumlahBarang = models.CharField()
    KondisiBarang = models.CharField(max_length=6, choices=choices)

    class Meta:
        db_table = 'sarpras'
        