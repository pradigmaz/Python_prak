from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_page, {"page_url": ""}, name='home'),
    path('<str:page_url>/', views.show_page, name='page'),
]
