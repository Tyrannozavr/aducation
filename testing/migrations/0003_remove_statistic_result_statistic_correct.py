# Generated by Django 4.1.3 on 2022-12-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_alter_attempts_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistic',
            name='result',
        ),
        migrations.AddField(
            model_name='statistic',
            name='correct',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
