# Generated by Django 4.2.15 on 2024-09-15 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juego.game')),
            ],
        ),
    ]
