# Generated by Django 3.0 on 2020-08-31 06:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourPlan', '0005_delete_memo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('plan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourPlan.Plan')),
            ],
        ),
    ]