# Generated by Django 4.1.10 on 2023-08-23 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_totaluser_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TotalUser',
        ),
        migrations.AlterField(
            model_name='userlogindata',
            name='email_validation_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.emailvalidationstatus'),
        ),
    ]
