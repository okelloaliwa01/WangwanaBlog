# Generated by Django 3.0.7 on 2020-07-05 03:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OwnTrackLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=100, verbose_name='user')),
                ('lat', models.FloatField(verbose_name='latitude')),
                ('lon', models.FloatField(verbose_name='longitude')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time')),
            ],
            options={
                'verbose_name': 'OwnTrackLogs',
                'verbose_name_plural': 'OwnTrackLogs',
                'ordering': ['created_time'],
                'get_latest_by': 'created_time',
            },
        ),
    ]
