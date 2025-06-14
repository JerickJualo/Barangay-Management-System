# Generated by Django 5.2 on 2025-05-22 01:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('residents', '0002_alter_resident_contact_number_alter_resident_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='email_address',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='resident',
            name='purok_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purok', to='residents.purok'),
        ),
    ]
