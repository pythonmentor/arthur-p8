# Generated by Django 3.0.7 on 2020-06-27 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0015_auto_20200627_1748'),
        ('favor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favor',
            name='substitute_of',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='substitute_of_set', to='foodfinder.Food'),
            preserve_default=False,
        ),
    ]
