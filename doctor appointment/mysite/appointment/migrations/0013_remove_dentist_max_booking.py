# Generated by Django 2.1.4 on 2019-01-02 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0012_auto_20190102_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dentist',
            name='max_booking',
        ),
    ]
