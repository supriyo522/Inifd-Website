from django.urls import path

from . import views
app_name = 'lp'
urlpatterns = [
    path('index/', views.index, name='index'),
]
