from django.urls import path
from . import views
from main_app.views import MineralCreate

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('minerals/', views.minerals_index, name='index'),
    # path('minerals/', MineralList.as_view(), name='index'),
    path('minerals/<int:mineral_id>/', views.minerals_detail, name='detail'),
    path('minerals/create', views.MineralCreate.as_view(), name='minerals_create'),
    path('minerals/<int:pk>/update', views.MineralUpdate.as_view(), name='minerals_update'),
    path('minerals/<int:pk>/delete', views.MineralDelete.as_view(), name='minerals_delete'),
]