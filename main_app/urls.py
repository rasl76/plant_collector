from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'), 
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_debug/', views.add_debug, name='add_debug'),
    path('plants/<int:plant_id>/assoc_light/<int:light_id>/', views.assoc_light, name='assoc_light'),
    path('plants/<int:plant_id>/unassoc_light/<int:light_id>/', views.unassoc_light, name='unassoc_light'),
    path('lights/', views.LightList.as_view(), name='lights_index'),
    path('lights/<int:pk>/', views.LightDetail.as_view(), name='lights_detail'),
    path('lights/create/', views.LightCreate.as_view(), name='lights_create'),
    path('lights/<int:pk>/update/', views.LightUpdate.as_view(), name='lights_update'),
    path('lights/<int:pk>/delete/', views.LightDelete.as_view(), name='lights_delete'),
    path('accounts/signup/', views.signup, name='signup'), 
]

