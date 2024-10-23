from django.db import models

# Create your models here.
class posbindu(models.Model):
    IdBindu = models.AutoField(primary_key=True)
    NamaBindu = models.CharField(max_length=64)
    AlamatBindu = models.CharField()
    BeratBindu = models.CharField()
    TekananDarahBindu= models.CharField()
    KeluhanBindu = models.CharField()
    
    # def __str__(self):
    #     return self.NamaBayi


    class Meta:
        db_table = 'posbindu'