# Generated by Django 4.1.3 on 2022-12-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_remove_statistic_result_statistic_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistic',
            name='wrong',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
