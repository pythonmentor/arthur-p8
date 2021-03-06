# Generated by Django 3.0.7 on 2020-06-14 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder', '0006_auto_20200614_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='nutriment_set',
        ),
        migrations.CreateModel(
            name='FoodNutriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_nutriment_set', to='foodfinder.Food')),
                ('nutriment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodfinder.Nutriment')),
            ],
        ),
    ]
