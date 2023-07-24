# Generated by Django 2.2.4 on 2023-06-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_pie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pie',
            name='value',
        ),
        migrations.AddField(
            model_name='pie',
            name='vote',
            field=models.ManyToManyField(default=0, related_name='voted_pies', to='login.User'),
        ),
    ]