# Generated by Django 3.0 on 2020-10-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourPlan', '0008_plan_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='scrap_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
