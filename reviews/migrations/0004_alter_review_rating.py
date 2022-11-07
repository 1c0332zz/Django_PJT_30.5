# Generated by Django 3.2.13 on 2022-11-05 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, '🍚'), (2, '🍚☕️'), (3, '🍚☕️🍷'), (4, '🍚☕️🍷🍰'), (5, '🍚☕️🍷🍰🍔')], default=None),
        ),
    ]
