from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(
        db_index=True, unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    second_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True, null=True)
    

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.email
