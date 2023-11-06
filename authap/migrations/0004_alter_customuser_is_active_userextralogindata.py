# Generated by Django 4.1.10 on 2023-10-14 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authap', '0003_customuser_dob_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserExtraLoginData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_validation_status', models.BooleanField(default=False)),
                ('confirmation_token', models.CharField(max_length=101)),
                ('token_generation_time', models.TimeField()),
                ('password_recovery_token', models.CharField(max_length=101)),
                ('recovery_token_time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authap.customuser')),
            ],
        ),
    ]
