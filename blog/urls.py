from django.urls import path

from blog import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.cagegories_page),
    path('tag/<str:slug>/', views.show_tag_posts)
]
