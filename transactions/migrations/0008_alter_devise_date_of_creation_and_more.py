# Generated by Django 5.0.9 on 2024-12-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0007_alter_transaction_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devise',
            name='date_of_creation',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devise',
            name='date_of_update',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_of_creation',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date_of_update',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_of_creation',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_of_update',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='date_of_creation',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactionhistory',
            name='date_of_update',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
