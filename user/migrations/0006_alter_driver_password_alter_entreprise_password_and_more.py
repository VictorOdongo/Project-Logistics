# Generated by Django 4.2.1 on 2023-05-26 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_entreprise_businesssize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='password',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='personal',
            name='password',
            field=models.CharField(),
        ),
    ]
