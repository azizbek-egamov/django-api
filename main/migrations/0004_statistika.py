# Generated by Django 4.2.11 on 2024-06-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_kitob_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitoblar_soni', models.IntegerField()),
            ],
        ),
    ]
