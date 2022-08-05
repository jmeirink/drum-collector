from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('drums/', views.drums_index, name='drums_index'),
  path('drums/<int:drum_id>/', views.drums_detail, name='drums_detail'),
]