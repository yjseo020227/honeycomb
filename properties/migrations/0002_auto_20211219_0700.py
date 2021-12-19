# Generated by Django 3.2.9 on 2021-12-19 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211219_0657'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commerical',
            name='landlord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.landlord'),
        ),
        migrations.AddField(
            model_name='residential',
            name='landlord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.landlord'),
        ),
    ]
