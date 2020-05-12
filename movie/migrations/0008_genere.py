# Generated by Django 3.0.2 on 2020-05-06 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200506_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='genere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A', 'action'), ('D', 'drama'), ('C', 'comedy'), ('R', 'romance')], max_length=150)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generes', to='movie.Movie')),
            ],
        ),
    ]