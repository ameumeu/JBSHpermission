# Generated by Django 4.1.1 on 2022-09-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_remove_user_is_permitted_user_permitted_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='period_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='period_2',
            field=models.BooleanField(default=False),
        ),
    ]
