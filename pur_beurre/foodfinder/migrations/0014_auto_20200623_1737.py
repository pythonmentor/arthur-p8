# Generated by Django 3.0.7 on 2020-06-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0013_auto_20200616_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutriment',
            name='name',
            field=models.CharField(max_length=127, unique=True),
        ),
    ]
