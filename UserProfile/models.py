from django.db import models
# from django.contrib import auth

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class UserProfileManager(BaseUserManager):
    """ User Manager for overridden class """
    def create(self,email, name, password = None):
        """ Create a new user Profile """
        if not email:
            raise ValueError("Email address field cannot be blank")  
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name)
        user.set_password(password)
        user.save(using = self._db)

        return user
    def createsuperuser(self, email, name, password):
        """ Create a super user """
        user = self.create(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using =  self._db)
        return user

    def __str__(self):
        return "@{}".format(self.email)
    




class UserModel(AbstractBaseUser,PermissionsMixin):
    """ Overridden User Model """
    email = models.EmailField(max_length = 255, unique = True)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def get_full_name(self):
        """Retreive full name of User """
        return self.name
    
    def get_short_name(self):
        """Retreive short name of User """
        return self.name

    def __str__(self):
        return "@{}".format(self.email)
    



class ProfileFeed(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
