# Generated by Django 4.2.1 on 2023-05-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_personal_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
