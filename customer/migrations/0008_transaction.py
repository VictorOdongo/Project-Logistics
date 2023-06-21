# Generated by Django 4.2.1 on 2023-06-21 11:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_job_distance_job_duration_job_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_payment_intent_id', models.CharField(max_length=255, unique=True)),
                ('amount', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.job')),
            ],
        ),
    ]
