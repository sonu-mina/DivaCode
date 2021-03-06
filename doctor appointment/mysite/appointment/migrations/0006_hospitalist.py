# Generated by Django 2.1.4 on 2018-12-31 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_gynecologist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospitalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('location', models.CharField(max_length=50)),
                ('available_dates', models.CharField(max_length=200)),
                ('works_from', models.IntegerField()),
                ('works_upto', models.IntegerField()),
                ('init_date', models.IntegerField(default=1)),
            ],
        ),
    ]
