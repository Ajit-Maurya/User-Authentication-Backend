# Generated by Django 4.1.10 on 2023-08-23 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_alter_emailvalidationstatus_email_validation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogindata',
            name='email_validation_status',
            field=models.BooleanField(),
        ),
        migrations.DeleteModel(
            name='EmailValidationStatus',
        ),
    ]
