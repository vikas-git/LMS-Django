# Generated by Django 2.0.5 on 2019-03-20 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('role', models.IntegerField(blank=True, choices=[(1, 'Student'), (2, 'Faculty'), (3, 'Admin')], help_text='1->Student, 2->Faculty 3->Admin', null=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]