# Generated by Django 2.2.6 on 2021-04-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_sorting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorting',
            name='sort_field',
            field=models.CharField(choices=[('created', 'По дате'), ('template', 'По типу блока')], default='created', max_length=30),
        ),
    ]
