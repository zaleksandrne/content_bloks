# Generated by Django 2.2.6 on 2021-04-20 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210420_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block_3',
            name='cost',
        ),
    ]