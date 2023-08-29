# Generated by Django 4.1.10 on 2023-08-23 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_delete_userlogindata'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailValidationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_validation_status', models.BooleanField(default=False)),
                ('status_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogInData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_hash', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('confirmation_token', models.CharField(max_length=100)),
                ('token_generation_time', models.TimeField()),
                ('password_recovery_token', models.CharField(max_length=100)),
                ('recovery_token_time', models.TimeField()),
                ('email_validation_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.emailvalidationstatus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.useraccount')),
            ],
        ),
    ]