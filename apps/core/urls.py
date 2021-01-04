#-*- coding: utf-8 -*-
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('file-create/', views.files_create, name='file-create'),
    path('file-update/<int:pk>/', views.files_update, name='file-update'),
    path('file-delete/<int:pk>/', views.files_delete, name='file-delete'),
]