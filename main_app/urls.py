from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('drums/', views.drums_index, name='drums_index'),
  path('drums/<int:drum_id>/', views.drums_detail, name='drums_detail'),
  path('drums/create/', views.DrumCreate.as_view(), name='drums_create'),
  path('drums/<int:pk>/update/', views.DrumUpdate.as_view(), name='drums_update'),
  path('drums/<int:pk>/delete/', views.DrumDelete.as_view(), name='drums_delete'),
]