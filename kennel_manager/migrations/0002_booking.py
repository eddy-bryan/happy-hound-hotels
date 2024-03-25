# Generated by Django 4.2.11 on 2024-03-25 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_management', '0002_petprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kennel_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Confirmed'), (2, 'Cancelled')], default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kennel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kennel_manager.kennel')),
                ('pet_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account_management.petprofile')),
            ],
        ),
    ]
