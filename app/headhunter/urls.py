from django.urls import path

from headhunter.views.headhunter import VacancyListView

urlpatterns = [
    path('', VacancyListView.as_view()),
    path('headhunter/', VacancyListView.as_view(), name='home_page'),
]
