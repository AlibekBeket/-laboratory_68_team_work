from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class VacancyCategory(models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        null=False,
        blank=False,
        max_length=100
    )

    class Meta:
        verbose_name = 'Категория вакансии'
        verbose_name_plural = 'Категории вакансий'

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    vacancy_category = models.ForeignKey(
        to='headhunter.VacancyCategory',
        verbose_name='Категория вакансии',
        on_delete=models.CASCADE,
        related_name='vacancies'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='vacancies',
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=False,
        blank=False
    )
    salary = models.PositiveIntegerField(
        verbose_name='Зарплата',
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name='Детальное описание',
        null=False,
        blank=False,
    )
    experience_time = models.PositiveIntegerField(
        verbose_name='Опыт работы (лет)',
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        verbose_name='Опубликовать вакансию',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False)

    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f"{self.author} - {self.name}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"