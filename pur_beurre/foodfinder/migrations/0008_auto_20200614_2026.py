# Generated by Django 3.0.7 on 2020-06-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0007_auto_20200614_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='nutriment_set',
            field=models.ManyToManyField(to='foodfinder.Nutriment'),
        ),
        migrations.AddField(
            model_name='nutriment',
            name='quantity',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='FoodNutriment',
        ),
    ]