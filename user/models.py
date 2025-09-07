from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from abstract.models import AbstractModel

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """Creating a user with username, email and passowrd"""
        if username is None:
            raise TypeError('Username required')
        if email is None:
            raise TypeError('Email required')
        if password is None:
            raise TypeError('Password required')
        user = self.model(username=username, 
            email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        "Create a user with admin permissions"
        if username is None:
            raise TypeError('Username required')

        if password is None:
            raise TypeError('Password required')
        if email is None:
            raise TypeError('Email required')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractModel, AbstractBaseUser, PermissionsMixin): 
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True) 

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"    

    objects = UserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name






        
    
        
        
