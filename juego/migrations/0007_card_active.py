# Generated by Django 4.2.15 on 2024-09-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0006_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
