from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.home, name='home'),  # Default view
    path('', views.survey_list, name='survey_list'),
    path('create/', views.survey_create, name='survey_create'),
    path('<int:survey_id>/questions/', views.question_list, name='question_list'),
    path('<int:survey_id>/questions/create/', views.question_create, name='question_create'),
    path('<int:survey_id>/respond/', views.response_create, name='response_create'),
    path('<int:survey_id>/results/', views.survey_results, name='survey_results'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
]
