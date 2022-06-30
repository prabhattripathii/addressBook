from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageFun),
    path('addnew', views.AddNewFun),
    path('search', views.SearchFun)
]
