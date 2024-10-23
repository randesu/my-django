# Generated by Django 5.1.1 on 2024-10-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imunisasi',
            fields=[
                ('IdAnak', models.AutoField(primary_key=True, serialize=False)),
                ('NamaAnak', models.CharField(max_length=64)),
                ('VaksinKe', models.CharField()),
                ('JenisVaksin', models.CharField()),
            ],
            options={
                'db_table': 'imunisasi',
            },
        ),
    ]