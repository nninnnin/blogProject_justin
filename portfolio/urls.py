from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/portfolio/', views.home, name="portfolio"),
    path('blog/portfolio/<int:portfolio_id>/', views.detail, name="pfdetail"),
]
