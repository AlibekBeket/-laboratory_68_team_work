from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices


class RoleChoice(TextChoices):
    EMPLOYER = 'employer', 'работодатель'
    APPLICANT = 'applicant', 'соискатель'


class Account(AbstractUser):
    user_role = models.CharField(
        verbose_name='Категория пользователя',
        choices=RoleChoice.choices,
        max_length=100,
        null=False,
        blank=False,
    )
    username = models.CharField(
        verbose_name='Имя',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False
    )
    phone = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )
    avatar = models.ImageField(
        null=False,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='avatars/default-user.png'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
