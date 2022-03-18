from django.urls import path

from blog import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
]
