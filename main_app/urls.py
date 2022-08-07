from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('drums/', views.drums_index, name='drums_index'),
  path('drums/<int:drum_id>/', views.drums_detail, name='drums_detail'),
  path('drums/create/', views.DrumCreate.as_view(), name='drums_create'),
  path('drums/<int:pk>/update/', views.DrumUpdate.as_view(), name='drums_update'),
  path('drums/<int:pk>/delete/', views.DrumDelete.as_view(), name='drums_delete'),
  path('drums/<int:drum_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
  path('accessories/create/', views.AccessoryCreate.as_view(), name='accessories_create'),
  path('accessories/<int:pk>/', views.AccessoryDetail.as_view(), name='accessories_detail'),
  path('accessories/', views.AccessoryList.as_view(), name='accessories_index'),
  path('accessories/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessories_update'),
  path('accessories/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessories_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]
