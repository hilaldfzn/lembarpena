# Generated by Django 4.2.6 on 2023-10-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('voters', models.IntegerField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=20)),
                ('decscription', models.TextField()),
                ('publisher', models.CharField(max_length=300)),
                ('page_count', models.IntegerField()),
            ],
        ),
    ]
