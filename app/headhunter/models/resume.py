from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class Experience(models.Model):
    company = models.CharField(
        verbose_name='Название организации',
        max_length=300,
        null=True,
        blank=False
    )
    start_date = models.DateField(
        verbose_name='Начало работы',
        max_length=100,
        null=True,
        blank=False
    )
    job_title = models.CharField(
        verbose_name='Должность',
        max_length=300,
        null=True,
        blank=False,
    )
    end_date = models.DateField(
        verbose_name='Окончание работы',
        max_length=100,
        null=True,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.company}, {self.job_title}, {self.start_date} - {self.end_date}'

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class CategoryEducationChoices(TextChoices):
    AVERAGE = 'average', 'Среднее'
    SECONDARY = 'secondary special', 'Среднее специальное'
    HIGHER = 'higher', 'Высшее  образование'
    MASTER = 'master', 'Магистратура'
    OTHER = 'other', 'Другое'


class Education(models.Model):
    institution_name = models.CharField(
        verbose_name='Учебное заведения',
        max_length=300,
        null=True,
        blank=False
    )
    speciality = models.CharField(
        verbose_name='Специальность',
        max_length=300,
        null=True,
        blank=False
    )
    category_education = models.CharField(
        verbose_name='Категория образования',
        choices=CategoryEducationChoices.choices,
        max_length=100,
        null=True,
        blank=False,
    )
    start_date = models.DateField(
        verbose_name='Начало обучения',
        max_length=100,
        null=True,
        blank=False
    )
    finish_date = models.DateField(
        verbose_name='Окончание обучения',
        max_length=100,
        null=True,
        blank=False
    )
    faculty = models.CharField(
        verbose_name='Факультет',
        max_length=200,
        null=True,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.institution_name} {self.speciality} {self.finish_date} '

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'


class Resume(models.Model):
    experience = models.ManyToManyField(
        to='headhunter.Experience',
        verbose_name='Опыт работы',
        related_name='experience',
        blank=True,
    )
    education = models.ManyToManyField(
        to='headhunter.Education',
        verbose_name='Образование',
        related_name='education',
        blank=True,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False
    )
    author = models.ForeignKey(
        verbose_name='Автор резюме',
        to=get_user_model(),
        related_name='resumes',
        blank=True,
        on_delete=models.CASCADE
    )
    salary = models.FloatField(
        verbose_name='Желаемая зарплата',
        null=False,
        blank=False
    )
    info = models.TextField(
        verbose_name='Информация о себе',
        max_length=3000,
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        null=False,
        blank=False,
    )
    phone = models.CharField(
        max_length=12,
        null=False,
        blank=False,
        verbose_name='Номер телефона'
    )
    telegram = models.CharField(
        verbose_name='Telegram',
        max_length=200,
        null=False,
        blank=False
    )
    linkedin = models.CharField(
        verbose_name='Linkedin',
        max_length=200,
        null=True,
        blank=True
    )
    facebook = models.CharField(
        verbose_name='Facebook',
        max_length=200,
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        verbose_name='Опубликовать резюме',
        default=False,
        null=False
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.name} Автор: {self.author}. Желаемая зарплата: {self.salary}'

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
