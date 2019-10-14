from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/delete/<int:post_pk>/', views.post_delete, name='post_delete'),
    path('post/edit/<int:post_pk>/', views.post_edit, name='post_edit'),
    path('post/<username>/<int:pk>/<slug:slug>/', views.post_detail, name='post_detail'),
]

