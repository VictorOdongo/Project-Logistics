# Generated by Django 4.2.1 on 2023-05-31 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_personal_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Personal',
        ),
    ]