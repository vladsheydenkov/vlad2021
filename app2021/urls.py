from django.urls import path
from . import views

app_name = 'task_app'


urlpatterns = [
    path('', views.main, name='main'),
    path('materials/', views.all_materials, name='all_materials'),
]
