# Generated by Django 5.1.1 on 2024-09-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jadwalKegiatan',
            fields=[
                ('IdKegiatan', models.AutoField(primary_key=True, serialize=False)),
                ('TanggalKegiatan', models.DateField()),
                ('NamaKegiatan', models.CharField()),
            ],
            options={
                'db_table': 'jadwalKegiatan',
            },
        ),
    ]