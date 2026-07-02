from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/<str:message>/', views.teacher_list, name='list'),
    path('form/', views.teacher_form, name='form'),
]