from django.views.generic import ListView

from headhunter.models import Vacancy


class VacancyListView(ListView):
    template_name = 'home_page.html'
    model = Vacancy
    context_object_name = 'vacancies'
    ordering = ('updated_at',)
