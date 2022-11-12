from django.urls import path
from . import views


app_name = 'upload'
urlpatterns = [
    path('', views.FileFieldFormView.as_view(), name='index'),
    path('success/', views.success, name='success')
]
