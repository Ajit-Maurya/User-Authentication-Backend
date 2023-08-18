from djongo import models
# Create your models here.

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
    # user_id = models.IntegerField()
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

# class HashingAlgo(models.Model):
#     hashing_algorithm_id = models.IntegerField()
#     algorithm_name = models.CharField(max_length=100)

class EmailValidationStatus(models.Model):
    email_validation_status = models.BooleanField(default=False)
    status_description = models.CharField(max_length=255)

class UserLogInData(models.Model):
    user_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    login_name  = models.CharField(max_length=30)
    password_hash = models.CharField(max_length=255)
    # password_salt = models.CharField(max_length=100)
    # hash_algorithm_id = models.ForeignKey(HashingAlgo,on_delete=models.PROTECT)
    email_address = models.EmailField()
    confirmation_token = models.CharField(max_length=100)
    token_generation_time = models.TimeField()
    email_validation_status = models.ForeignKey(EmailValidationStatus,on_delete=models.CASCADE)
    password_recovery_token = models.CharField(max_length=100)
    recovery_token_time = models.TimeField()

    def __str__(self) -> str:
        return self.login_name

class UserLoginDataExternal(models.Model):
    user_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE)
    external_provided_id = models.IntegerField()
    external_provided_token = models.CharField(max_length=100)

