# Generated by Django 5.1.3 on 2024-11-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userregistrationmodel_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Homme'), ('F', 'Femme')], max_length=1, null=True),
        ),
    ]
