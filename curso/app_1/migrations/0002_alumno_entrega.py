# Generated by Django 5.1.4 on 2024-12-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20)),
                ('apellido', models.CharField(blank=True, max_length=20)),
                ('edad', models.IntegerField(blank=True)),
                ('matricula', models.IntegerField()),
                ('promedio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20)),
                ('fecha_de_entrega', models.DateField()),
            ],
        ),
    ]