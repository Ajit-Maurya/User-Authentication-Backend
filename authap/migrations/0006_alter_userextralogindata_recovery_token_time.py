# Generated by Django 4.1.10 on 2023-10-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authap', '0005_alter_userextralogindata_token_generation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextralogindata',
            name='recovery_token_time',
            field=models.DateTimeField(),
        ),
    ]
