# Generated by Django 3.1 on 2021-03-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210329_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='points',
            field=models.IntegerField(),
        ),
    ]
