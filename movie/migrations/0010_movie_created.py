# Generated by Django 3.0.2 on 2020-05-07 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 7, 12, 56, 14, 743795)),
        ),
    ]
