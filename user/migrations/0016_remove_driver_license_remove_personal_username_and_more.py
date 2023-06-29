# Generated by Django 4.2.1 on 2023-06-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_delete_entreprise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='license',
        ),
        migrations.RemoveField(
            model_name='personal',
            name='username',
        ),
        migrations.AddField(
            model_name='driver',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]