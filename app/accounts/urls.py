from django.urls import path

from accounts.views import RegisterView, LoginView, logout_view, UserChangeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
]
