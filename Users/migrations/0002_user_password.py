# Generated by Django 4.0.2 on 2022-02-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=95797),
        ),
    ]