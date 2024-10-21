# Generated by Django 5.1.2 on 2024-10-17 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('genero_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_genero', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('Usuarios_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]