from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# import the Base user model
from django.contrib.auth.models import AbstractBaseUser
# importing Permissions - to be added to base user-model
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Helps Django work with our custom user model."""

    # on how to create user
    def create_user(self, email, name, password=None):
        """Creates a new user profile object. """
        if not email:
            raise ValueError('Users must have an email address.')
        #normalizing email address
        email = self.normalize_email(email)
        #create the user entry
        user = self.model(email=email, name = name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ Creates and saves a new Superuser with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user




# substituting with a custom user-modal

# Create your models here.

# you define model as a class

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name =  models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # required

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Helper functions
    def get_full_name(self): # used by Django Admin
        """Used to get a user's full name."""
        return self.name

    def get_short_name(self):
        """Used to get a users's short name"""
        return self.name

    def __str__(self):
        """ Django uses this when it needs to convert the object to a string"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profiles status update."""
    # if user deletes his profile delete all status updates of that deleted user
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""

        return self.status_text 
