# Generated by Django 3.0.7 on 2020-07-05 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=300, verbose_name='text')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Change time')),
                ('is_enable', models.BooleanField(default=True, verbose_name='Whether to show')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article', verbose_name='article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comments.Comment', verbose_name='Superior comment')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comment',
                'ordering': ['id'],
                'get_latest_by': 'id',
            },
        ),
    ]
