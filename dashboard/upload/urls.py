from django.urls import path
from . import views


app_name = 'upload'
urlpatterns = [
    path('', views.index, name='index'),
    path('latest_uploads/', views.latest_uploads, name='latest_uploads'),
    path('alternative_upload/', views.alternative_upload, name='alt')
]