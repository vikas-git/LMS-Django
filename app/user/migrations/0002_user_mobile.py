# Generated by Django 2.0.5 on 2019-03-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]