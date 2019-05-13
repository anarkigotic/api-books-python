# Generated by Django 2.2.1 on 2019-05-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
