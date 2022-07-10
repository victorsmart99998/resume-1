from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.home, name="home"),
    path('info/',views.info,name="info"),
    path('', views.main, name="profile")
]
