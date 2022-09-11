# Generated by Django 4.1.1 on 2022-09-11 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0004_remove_permission_classroom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('headcount', models.IntegerField(default=0)),
            ],
        ),
    ]
