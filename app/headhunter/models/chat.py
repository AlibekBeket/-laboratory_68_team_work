from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class ApplicantEmployer(models.Model):
    applicant = models.ForeignKey(
        verbose_name='Соискатель',
        to=get_user_model(),
        related_name='applicant',
        blank=False,
        on_delete=models.CASCADE
    )
    employer = models.ForeignKey(
        verbose_name='Работодатель',
        to=get_user_model(),
        related_name='employer',
        blank=False,
        on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        verbose_name='Вакансия',
        to='headhunter.Vacancy',
        related_name='vacancy',
        blank=False,
        on_delete=models.CASCADE
    )
    resume = models.ForeignKey(
        verbose_name='Резюме',
        to='headhunter.Resume',
        related_name='resume',
        blank=False,
        on_delete=models.CASCADE
    )
    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.applicant.username} - {self.employer.username} chat'


class ApplicantEmployerChoices(TextChoices):
    APPLICANT = 'applicant', 'Соискатель'
    EMPLOYER = 'employer', 'Работодатель'


class Chat(models.Model):
    applicant_employer_pk = models.ForeignKey(
        verbose_name='Чат между',
        to=ApplicantEmployer,
        related_name='applicant_employer',
        blank=False,
        on_delete=models.CASCADE
    )
    applicant_or_employer = models.ForeignKey(
        verbose_name='Кто отправитель',
        choices=ApplicantEmployerChoices.choices,
        max_length=100,
        null=False,
        blank=False
    )
    text = models.TextField(
        verbose_name='Текст сообщения',
        max_length=20000,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата отправки',
        auto_now_add=True
    )
    deleted_at = models.DateTimeField(
        verbose_name='Время удаления',
        null=True,
        default=None
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'chat id {self.applicant_employer_pk} - sender {self.applicant_or_employer}'
