from django.contrib import admin
from headhunter.models.vacancy import Vacancy, VacancyCategory


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'salary', 'description', 'experience_time', 'is_active', 'created_at',
                    'updated_at', 'vacancy_category', 'is_deleted')
    list_filter = ('author', 'name', 'salary', 'is_active', 'created_at', 'updated_at', 'vacancy_category')
    search_fields = ('author', 'name', 'salary', 'is_active', 'created_at', 'updated_at', 'vacancy_category')
    fields = ('author', 'name', 'salary', 'description', 'experience_time', 'is_active', 'vacancy_category')
    readonly_fields = ['id']


admin.site.register(VacancyCategory)
admin.site.register(Vacancy, VacancyAdmin)
