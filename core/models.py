from django.db import models
from django.contrib.auth.models import AbstractUser

# Iheriting the abstract user and adding functionality like adding the email to be required and unique it is not unique and required in django abstract user


class User(AbstractUser):
    email = models.EmailField(unique=True)
