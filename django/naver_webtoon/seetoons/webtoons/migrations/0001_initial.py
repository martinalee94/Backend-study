# Generated by Django 4.0 on 2021-12-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webtoons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=80)),
                ('img', models.TextField()),
            ],
        ),
    ]
