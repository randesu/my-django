# Generated by Django 5.1.1 on 2024-09-26 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sarpras',
            fields=[
                ('IdBarang', models.AutoField(primary_key=True, serialize=False)),
                ('NamaBarang', models.CharField()),
                ('JumlahBarang', models.CharField()),
                ('KondisiBarang', models.CharField()),
            ],
            options={
                'db_table': 'sarpras',
            },
        ),
    ]