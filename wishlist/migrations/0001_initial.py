<<<<<<< HEAD
# Generated by Django 4.2.6 on 2023-10-26 05:01

from django.conf import settings
=======
# Generated by Django 4.2.6 on 2023-10-24 15:14

>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registerbook', '0001_initial'),
=======
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
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
=======
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('preference', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registerbook.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
=======
                ('like_scale', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('goal', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wishlist.book')),
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
            ],
        ),
    ]
