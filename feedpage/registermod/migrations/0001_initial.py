# Generated by Django 5.0 on 2023-12-17 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registermod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=50)),
                ('ea', models.EmailField(max_length=254)),
                ('pa', models.CharField(max_length=50)),
            ],
        ),
    ]
