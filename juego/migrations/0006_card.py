# Generated by Django 4.2.15 on 2024-09-16 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0005_player_coordinate_x_player_coordinate_y'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('challenge', 'Reto'), ('true', 'Verdad'), ('question', 'Pregunta'), ('penalty', 'Castigo')], max_length=20)),
                ('text', models.CharField(max_length=300)),
            ],
        ),
    ]
