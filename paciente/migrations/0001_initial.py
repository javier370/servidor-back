# Generated by Django 4.2.5 on 2023-10-16 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('documento', models.IntegerField()),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
                ('zona_residencial', models.CharField(max_length=50)),
                ('estado_civil', models.CharField(max_length=50)),
                ('rh', models.CharField(max_length=3)),
                ('credo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
    ]
