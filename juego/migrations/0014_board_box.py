# Generated by Django 4.2.15 on 2024-09-19 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0013_player_winer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_number', models.IntegerField(default=8)),
                ('row_number', models.IntegerField(default=8)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='juego.game')),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juego.board')),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='juego.card')),
            ],
        ),
    ]
