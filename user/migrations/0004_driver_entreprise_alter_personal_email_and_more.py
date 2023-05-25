# Generated by Django 4.2.1 on 2023-05-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_personal_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('id', models.CharField(unique=True)),
                ('licence', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('businessname', models.CharField(max_length=20, unique=True)),
                ('businesssize', models.IntegerField(max_length=20)),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='personal',
            name='email',
            field=models.EmailField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='personal',
            name='password',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
