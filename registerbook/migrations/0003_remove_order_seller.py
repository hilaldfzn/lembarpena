# Generated by Django 4.2.4 on 2023-10-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerbook', '0002_auto_20231028_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
    ]