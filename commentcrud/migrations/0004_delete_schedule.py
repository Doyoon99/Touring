# Generated by Django 3.0 on 2020-09-04 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentcrud', '0003_schedule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]