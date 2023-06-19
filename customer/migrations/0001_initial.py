# Generated by Django 4.2.1 on 2023-06-15 13:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=20)),
                ('quantity', models.IntegerField(default=1)),
                ('photo', models.ImageField(upload_to='job/photos/')),
                ('status', models.CharField(choices=[('creating', 'Creating'), ('processing', 'Processing'), ('picking', 'Picking'), ('delivering', 'Delivering'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='creating', max_length=20)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.category')),
                ('customer_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]