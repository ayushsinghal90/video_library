# Generated by Django 3.2.4 on 2021-06-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('failed', 'FAILED'), ('success', 'SUCCESS')], default='success', max_length=200)),
                ('key', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Key',
                'verbose_name_plural': 'Keys',
                'db_table': 'key',
            },
        ),
        migrations.AddIndex(
            model_name='keys',
            index=models.Index(fields=['type'], name='key_type_6dc47c_idx'),
        ),
        migrations.AddIndex(
            model_name='keys',
            index=models.Index(fields=['id'], name='key_id_231203_idx'),
        ),
    ]