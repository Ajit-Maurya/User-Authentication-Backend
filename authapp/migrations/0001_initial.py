# Generated by Django 4.1.10 on 2023-08-13 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='ExternalProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_provider_id', models.IntegerField()),
                ('provider_name', models.CharField(max_length=30)),
                ('ws_Endpoint', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HashingAlgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashing_algorithm_id', models.IntegerField()),
                ('algorithm_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions_id', models.IntegerField()),
                ('permission_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=15)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField()),
                ('role_description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginDataExternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_provided_id', models.IntegerField()),
                ('external_provided_token', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.useraccount')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogInData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=30)),
                ('password_hash', models.CharField(max_length=255)),
                ('password_salt', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('confirmation_token', models.CharField(max_length=100)),
                ('token_generation_time', models.TimeField()),
                ('password_recovery_token', models.CharField(max_length=100)),
                ('recovery_token_time', models.TimeField()),
                ('email_validation_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.emailvalidationstatus')),
                ('hash_algorithm_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authapp.hashingalgo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.useraccount')),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authapp.userrole'),
        ),
        migrations.CreateModel(
            name='GrantedPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissions_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.permission')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.userrole')),
            ],
        ),
    ]
