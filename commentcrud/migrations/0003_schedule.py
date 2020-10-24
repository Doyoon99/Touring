# Generated by Django 3.0 on 2020-09-04 09:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tourPlan', '0005_delete_memo'),
        ('commentcrud', '0002_auto_20200902_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='일정')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='작성시간')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('plan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='tourPlan.Plan')),
            ],
        ),
    ]