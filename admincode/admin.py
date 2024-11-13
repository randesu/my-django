from django.contrib import admin
from unfold.admin import ModelAdmin
from datetime import datetime
from time import sleep
from csv2pdf import convert
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group


# Register your models here.
#from barangRental.models import barangRental

from anggota.models import anggotaPosyandu
from db_bayi.models import bayi
from db_jentik.models import rumahJentik
from jadwal_kegiatan.models import jadwalKegiatan
from jadwal_kunjungan.models import jadwalKunjungan
from kotaksaran.models import kotakSaran
from sarpras.models import sarpras
from db_ibuhamil.models import ibuHamil
from db_imunisasi.models import imunisasi
from db_posbindu.models import posbindu



admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

#------------ Define Action -------------#

#---- Section Anggota ----#
@admin.action(description="Print ke CLI")
def printAnggota(modeladmin, request, queryset):
    
    for f in queryset:
        
        print(f.IdAnggota,f.NamaAnggota)
        
    pass

@admin.action(description="Print ke CSV dengan Header")
def printAnggotaCSVHeader(modeladmin, request, queryset):
    fileName = "Anggota-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Id Anggota, Nama Anggota" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdAnggota,f.NamaAnggota)
        file = open(fileName, "a")
        file.write(str(f.IdAnggota) +','+ f.NamaAnggota + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printAnggotaCsvNoHeader(modeladmin, request, queryset):
    fileName = f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Id Anggota, Nama Anggota" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdAnggota,f.NamaAnggota)
        file = open(fileName, "a")
        file.write(str(f.IdAnggota) +','+ f.NamaAnggota + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()


@admin.action(description="Print ke PDF dengan header")
def printAnggotaPDF(modeladmin, request, queryset):
    fileName = "Anggota-"f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Id Anggota, Nama Anggota" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdAnggota,f.NamaAnggota)
        file = open(fileName, "a")
        file.write(str(f.IdAnggota) +','+ f.NamaAnggota + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Bayi ----#
@admin.action(description="Print ke CLI")
def printBayi(modeladmin, request, queryset):
    for f in queryset:
        print(f.IdBayi,f.NamaBayi)
    pass

@admin.action(description="Print ke CSV dengan Header")
def printBayiCSVHeader(modeladmin, request, queryset):
    fileName = "Bayi-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Id Bayi, Nama Bayi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdBayi,f.NamaBayi)
        file = open(fileName, "a")
        file.write(str(f.IdBayi) +','+ f.NamaBayi + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printBayiCsvNoHeader(modeladmin, request, queryset):
    fileName = "Bayi-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Id Bayi, Nama Bayi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdBayi,f.NamaBayi)
        file = open(fileName, "a")
        file.write(str(f.IdBayi) +','+ f.NamaBayi + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printBayiPDF(modeladmin, request, queryset):
    fileName = "Bayi-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Id Bayi, Nama Bayi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.IdBayi,f.NamaBayi)
        file = open(fileName, "a")
        file.write(str(f.IdBayi) +','+ f.NamaBayi + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Jentik ----#
@admin.action(description="Print ke CLI")
def printJentik(modeladmin, request, queryset):
    for f in queryset:
        print(f.NomorRumah,f.KepalaRumah, f.AlamatRumah, f.JumlahKontainer, f.KontainerJentik)
    pass

@admin.action(description="Print ke CSV dengan Header")
def printJentikCSVHeader(modeladmin, request, queryset):
    fileName = "Jentik-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Nomor Rumah, Kepala Rumah Tangga, Alamat Rumah, Jumlah Kontainer, Kontainer Berjentik" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.NomorRumah,f.KepalaRumah, f.AlamatRumah, f.JumlahKontainer, f.KontainerJentik)
        file = open(fileName, "a")
        file.write(f.NomorRumah +','+ f.KepalaRumah +','+ f.AlamatRumah +','+ f.JumlahKontainer +','+ f.KontainerJentik + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printJentikCsvNoHeader(modeladmin, request, queryset):
    fileName = "Jentik-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Nomor Rumah, Kepala Rumah Tangga, Alamat Rumah, Jumlah Kontainer, Kontainer Berjentik" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.NomorRumah,f.KepalaRumah, f.AlamatRumah, f.JumlahKontainer, f.KontainerJentik)
        file = open(fileName, "a")
        file.write(f.NomorRumah +','+ f.KepalaRumah +','+ f.AlamatRumah +','+ f.JumlahKontainer +','+ f.KontainerJentik + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printJentikPDF(modeladmin, request, queryset):
    fileName = "Jentik-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Nomor Rumah, Kepala Rumah Tangga, Alamat Rumah, Jumlah Kontainer, Kontainer Berjentik" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.NomorRumah,f.KepalaRumah, f.AlamatRumah, f.JumlahKontainer, f.KontainerJentik)
        file = open(fileName, "a")
        file.write(f.NomorRumah +','+ f.KepalaRumah +','+ f.AlamatRumah +','+ f.JumlahKontainer +','+ f.KontainerJentik + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Kegiatan ----#
@admin.action(description="Print ke CLI")
def printKegiatan(modeladmin, request, queryset):
    for f in queryset:
        print(f.TanggalKegiatan,f.NamaKegiatan)
    pass


@admin.action(description="Print ke CSV dengan Header")
def printKegiatanCSVHeader(modeladmin, request, queryset):
    fileName = "Kegiatan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Tanggal Kegiatan, Nama Kegiatan" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKegiatan,f.NamaKegiatan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKegiatan) +',' + f.NamaKegiatan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV Tanpa Header")
def printKegiatanCsvNoHeader(modeladmin, request, queryset):
    fileName = "Kegiatan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Tanggal Kegiatan, Nama Kegiatan" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKegiatan,f.NamaKegiatan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKegiatan) +',' + f.NamaKegiatan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printKegiatanPDF(modeladmin, request, queryset):
    fileName = "Kegiatan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Tanggal Kegiatan, Nama Kegiatan" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKegiatan,f.NamaKegiatan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKegiatan) +',' + f.NamaKegiatan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Kunjungan ----#
@admin.action(description="Print ke CLI")
def printKunjungan(modeladmin, request, queryset):
    for f in queryset:
        print(f.TanggalKunjungan,f.NamaKunjungan, f.DeskripsiKunjungan)
    pass

@admin.action(description="Print ke CSV dengan Header")
def printKunjunganCSVHeader(modeladmin, request, queryset):
    fileName = "Kunjungan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("Tanggal Kunjungan, Nama Kunjungan, Deskripsi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKunjungan,f.NamaKunjungan, f.DeskripsiKunjungan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKunjungan) +',' + f.NamaKunjungan +',' + f.DeskripsiKunjungan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printKunjunganCsvNoHeader(modeladmin, request, queryset):
    fileName = "Kunjungan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Tanggal Kunjungan, Nama Kunjungan, Deskripsi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKunjungan,f.NamaKunjungan, f.DeskripsiKunjungan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKunjungan) +',' + f.NamaKunjungan +',' + f.DeskripsiKunjungan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printKunjunganPDF(modeladmin, request, queryset):
    fileName = "Kunjungan-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("Tanggal Kunjungan, Nama Kunjungan, Deskripsi" + "\n")
    print("Created file")
    for f in queryset: 
        print(f.TanggalKunjungan,f.NamaKunjungan, f.DeskripsiKunjungan)
        file = open(fileName, "a")
        file.write(str(f.TanggalKunjungan) +',' + f.NamaKunjungan +',' + f.DeskripsiKunjungan + "\n") #write data with a newline
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Saran ----#
@admin.action(description="Print ke CLI")
def printSaran(modeladmin, request, queryset):
    for f in queryset:
        print(f.IsiSaran)
    pass

@admin.action(description="Print ke CSV dengan Header")
def printSaranCSVHeader(modeladmin, request, queryset):
    fileName = "Saran-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("No, Saran" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.IsiSaran)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.IsiSaran + "\n") #write data with a newline
        nomor = nomor + 1
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printSaranCsvNoHeader(modeladmin, request, queryset):
    fileName = "Saran-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("No, Saran" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.IsiSaran)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.IsiSaran + "\n") #write data with a newline
        nomor = nomor + 1
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printSaranPDF(modeladmin, request, queryset):
    fileName = "Saran-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("No, Saran" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.IsiSaran)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.IsiSaran + "\n") #write data with a newline
        nomor =  nomor + 1
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#---- Section Sarpras ----#
@admin.action(description="Print ke CLI")
def printSarpras(modeladmin, request, queryset):
    for f in queryset:
        print(f.NamaBarang,f.JumlahBarang, f.KondisiBarang)
    pass

@admin.action(description="ganti kondisi barang ke baik")
def make_published_baik(modeladmin, request, queryset):
    queryset.update(KondisiBarang="baik")

@admin.action(description="ganti kondisi barang ke sedang")
def make_published_sedang(modeladmin, request, queryset):
    queryset.update(KondisiBarang="sedang")

@admin.action(description="ganti kondisi barang ke buruk")
def make_published_buruk(modeladmin, request, queryset):
    queryset.update(KondisiBarang="buruk")

@admin.action(description="Print ke CSV dengan Header")
def printSarprasCSVHeader(modeladmin, request, queryset):
    fileName = "SaranaPrasarana-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("No, Nama Barang, Jumlah Barang, Kondisi Barang" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.NamaBarang,f.JumlahBarang, f.KondisiBarang)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.NamaBarang +',' + f.JumlahBarang +',' + f.KondisiBarang + "\n") #write data with a newline
        nomor = nomor + 1
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke CSV tanpa Header")
def printSarprasCsvNoHeader(modeladmin, request, queryset):
    fileName = "SaranaPrasarana-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    # file.write("No, Nama Barang, Jumlah Barang, Kondisi Barang" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.NamaBarang,f.JumlahBarang, f.KondisiBarang)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.NamaBarang +',' + f.JumlahBarang +',' + f.KondisiBarang + "\n") #write data with a newline
        nomor = nomor + 1
    pass
    print("Data collection complete!")
    file.close()

@admin.action(description="Print ke PDF dengan header")
def printSarprasPDF(modeladmin, request, queryset):
    fileName = "SaranaPrasarana-"+f"{datetime.now().strftime("%Y%m%d-%H%M%S")}"+".csv"
    print(fileName)
    file = open(fileName, "a")
    file.write("No, Nama Barang, Jumlah Barang, Kondisi Barang" + "\n")
    print("Created file")
    nomor = 1
    for f in queryset: 
        print(nomor, f.NamaBarang,f.JumlahBarang, f.KondisiBarang)
        file = open(fileName, "a")
        file.write(str(nomor) +',' + f.NamaBarang +',' + f.JumlahBarang +',' + f.KondisiBarang + "\n") #write data with a newline
        nomor = nomor + 1
    pass
    print("Data collection complete!")
    file.close()
    converted  = convert(fileName, fileName+".pdf")
    print(converted)


#-------------------- Classes -----------------#
class anggotaDisplay(ModelAdmin):
    list_display = ['IdAnggota', 'NamaAnggota']
    actions = [printAnggota, printAnggotaCSVHeader, printAnggotaCsvNoHeader, printAnggotaPDF]

class bayiDisplay(ModelAdmin):
    list_display = ['IdBayi', 'NamaBayi', 'TanggalLahir']
    actions = [printBayi, printBayiCSVHeader, printAnggotaCsvNoHeader, printBayiPDF]

class jentikDisplay(ModelAdmin):
    list_display = ['IdRumah', 'NomorRumah', 'KepalaRumah',
                    'AlamatRumah', 'JumlahKontainer', 'KontainerJentik']
    actions = [printJentik, printJentikCSVHeader, printJentikCsvNoHeader, printJentikPDF]

class kegiatanDisplay(ModelAdmin):
    list_display = ['IdKegiatan', 'TanggalKegiatan', 'NamaKegiatan']
    actions = [printKegiatan, printKegiatanCSVHeader, printKegiatanCsvNoHeader, printKegiatanPDF]

class kunjunganDisplay(ModelAdmin):
    list_display = ['IdKunjungan', 'TanggalKunjungan',
                    'NamaKunjungan', 'DeskripsiKunjungan']
    actions = [printKunjungan, printKunjunganCSVHeader, printKunjunganCsvNoHeader, printKunjunganPDF]

class saranDisplay(ModelAdmin):
    list_display = ['IdSaran', 'IsiSaran']
    actions = [printSaran, printSaranCSVHeader, printSaranCsvNoHeader, printSaranPDF]

class sarprasDisplay(ModelAdmin):
    list_display = ['IdBarang', 'NamaBarang',
                    'JumlahBarang', 'KondisiBarang']
    actions = [printSarpras, make_published_baik, make_published_buruk, make_published_sedang, printSarprasCSVHeader, printSarprasCsvNoHeader,
               printSarprasPDF]

class ibuHamilDisplay(ModelAdmin):
    list_display = ['IdIbu', 'NamaIbu',
                    'UmurKehamilan']

class imunisasiDisplay(ModelAdmin):
    list_display = ['IdAnak', 'NamaAnak', 'VaksinKe','JenisVaksin'
                    ]
    
class posbinduDisplay(ModelAdmin):
    list_display = ['IdBindu', 'NamaBindu','AlamatBindu', 'BeratBindu', 'TekananDarahBindu', 'KeluhanBindu']



#------------ app register ----------------#
admin.site.register(anggotaPosyandu, anggotaDisplay)
admin.site.register(bayi, bayiDisplay)
admin.site.register(rumahJentik, jentikDisplay)
admin.site.register(jadwalKegiatan,kegiatanDisplay)
admin.site.register(jadwalKunjungan,kunjunganDisplay)
admin.site.register(kotakSaran,saranDisplay)
admin.site.register(sarpras,sarprasDisplay)
admin.site.register(ibuHamil, ibuHamilDisplay)
admin.site.register(imunisasi, imunisasiDisplay)
admin.site.register(posbindu, posbinduDisplay)