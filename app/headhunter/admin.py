from django.contrib import admin

from headhunter.models.resume import Resume, CategoryEducationChoices, Education, Experience
from headhunter.models.vacancy import Vacancy, VacancyCategory


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'salary', 'description', 'experience_time', 'is_active', 'created_at',
                    'updated_at', 'vacancy_category', 'is_deleted', 'deleted_at')
    list_filter = ('author', 'name', 'salary', 'is_active', 'created_at', 'updated_at',
                   'vacancy_category')
    search_fields = ('author', 'name', 'salary', 'is_active', 'created_at', 'updated_at',
                     'vacancy_category')
    fields = ('author', 'name', 'salary', 'description', 'experience_time', 'is_active',
              'vacancy_category')
    readonly_fields = ['id']


admin.site.register(VacancyCategory)
admin.site.register(Vacancy, VacancyAdmin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'salary', 'info', 'email', 'phone', 'telegram', 'linkedin', 'facebook',
                    'is_published', 'created_at', 'updated_at', 'is_deleted', 'deleted_at')
    list_filter = ('name', 'author', 'salary', 'info', 'email', 'phone', 'telegram', 'linkedin', 'facebook',
                   'is_published', 'created_at', 'updated_at')
    search_fields = ('experience', 'education', 'name', 'author', 'info', 'email', 'phone', 'telegram', 'linkedin', 'facebook',
                     'is_published', 'created_at', 'updated_at')
    fields = ('experience', 'education', 'name', 'author', 'info', 'email', 'phone', 'telegram', 'linkedin', 'facebook', 'is_published')
    readonly_fields = ['id']


class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution_name', 'speciality', 'category_education', 'start_date', 'finish_date',
                    'faculty', 'created_at', 'updated_at')
    list_filter = ('institution_name', 'speciality', 'category_education', 'start_date', 'finish_date',
                   'faculty', 'created_at', 'updated_at')
    search_fields = ('institution_name', 'speciality', 'category_education', 'start_date', 'finish_date',
                     'faculty')
    fields = ('institution_name', 'speciality', 'category_education', 'start_date', 'finish_date',
              'faculty')
    readonly_fields = ['id']


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'start_date', 'end_date', 'created_at', 'updated_at')
    list_filter = ('company', 'job_title', 'start_date', 'end_date')
    search_fields = ('company', 'job_title', 'start_date', 'end_date')
    fields = ('company', 'job_title', 'start_date', 'end_date')
    readonly_fields = ['id']


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
