# Generated by Django 3.0 on 2020-09-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentcrud', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='content',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]