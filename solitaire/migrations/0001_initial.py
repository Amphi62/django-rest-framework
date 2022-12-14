# Generated by Django 4.1 on 2022-08-22 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolitaireGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('in-progress', 'In Progress'), ('surrender', 'Surrender'), ('win', 'Win'), ('loose', 'Loose'), ('initialize', 'Initialize')], default='initialize', max_length=25)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('hard', 'Hard')], default='easy', max_length=25)),
                ('is_timed', models.BooleanField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('slug', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
