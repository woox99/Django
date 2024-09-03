from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('clear-session/', views.clear_session, name='clear-session'),
]