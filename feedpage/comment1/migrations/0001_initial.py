# Generated by Django 5.0 on 2023-12-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment1_n', models.CharField(max_length=50)),
                ('comment1_d', models.TextField()),
            ],
        ),
    ]