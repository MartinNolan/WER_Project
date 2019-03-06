# Generated by Django 2.1.5 on 2019-03-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WER_app', '0004_auto_20190302_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(unique=True)),
                ('email', models.CharField(default='Defualt', max_length=100, unique=True)),
                ('password', models.CharField(default='Default', max_length=30)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]