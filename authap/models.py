from djongo import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.contrib.auth.models import Group,Permission
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email,password, **extra_fields)
    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permission',
        blank=True,
        related_name='custom_user'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email

class UserExtraLoginData(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email_validation_status = models.BooleanField(default=False)
    confirmation_token = models.CharField(max_length=101)
    token_generation_time = models.DateTimeField()
    password_recovery_token = models.CharField(max_length=101)
    recovery_token_time = models.DateTimeField()




































class UserRole(models.Model):
    role_id = models.IntegerField()
    role_description = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.role_description

class permission(models.Model):
    permissions_id = models.IntegerField()
    permission_description = models.CharField(max_length=255)

class GrantedPermission(models.Model):
    role_id = models.ForeignKey(UserRole,on_delete=models.CASCADE)
    permissions_id = models.ForeignKey(permission,on_delete=models.CASCADE)

class UserAccount(models.Model):
    first_name = models.CharField(max_length=30,db_index=True)
    last_name = models.CharField(max_length=30,db_index=True)
    gender = models.CharField(max_length=15,db_index=True)
    dob = models.DateField()
    role_id = models.ForeignKey(UserRole,on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.first_name

class ExternalProvider(models.Model):
    external_provider_id = models.IntegerField()
    provider_name = models.CharField(max_length=30)
    ws_Endpoint = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.provider_name

# class UserLogInData(models.Model):
#     user_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
#     password_hash = models.CharField(max_length=255)
#     email_address = models.EmailField()
#     confirmation_token = models.CharField(max_length=100)
#     token_generation_time = models.TimeField()
#     email_validation_status = models.BooleanField(default=False)
#     password_recovery_token = models.CharField(max_length=100)
#     recovery_token_time = models.TimeField()

    def __str__(self) -> str:
        return self.login_name
    
class UserLoginDataExternal(models.Model):
    user_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    external_provided_id = models.IntegerField()
    external_provided_token = models.CharField(max_length=100)