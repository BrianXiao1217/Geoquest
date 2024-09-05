# Generated by Django 4.2.4 on 2023-11-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_quest_cache_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='liked_quests',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to='maps.quest'),
        ),
    ]
