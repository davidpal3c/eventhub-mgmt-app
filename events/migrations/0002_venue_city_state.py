# Generated by Django 5.0.6 on 2024-05-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='city_state',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]