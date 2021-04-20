# Generated by Django 2.2.6 on 2021-04-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('action', models.CharField(max_length=500)),
                ('answer1', models.CharField(max_length=500)),
                ('answer2', models.CharField(max_length=500)),
                ('answer3', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Block_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=500)),
                ('main', models.CharField(max_length=500)),
                ('title2', models.CharField(max_length=500)),
                ('main2', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Block_3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('button', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('cost', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='LandingBlock',
        ),
        migrations.DeleteModel(
            name='LandingPage',
        ),
    ]