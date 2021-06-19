# Generated by Django 3.2.4 on 2021-06-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('channel_id', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channels',
                'db_table': 'channel',
            },
        ),
        migrations.AddIndex(
            model_name='channel',
            index=models.Index(fields=['name'], name='channel_name_73c842_idx'),
        ),
    ]