# Generated by Django 3.0 on 2020-08-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourPlan', '0002_memo'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
