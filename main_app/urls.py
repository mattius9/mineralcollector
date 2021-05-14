from django.urls import path
from . import views
from main_app.views import MineralList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('minerals/', views.minerals_index, name='index'),
    # path('minerals/', MineralList.as_view(), name='index'),
    path('minerals/<int:mineral_id>/', views.minerals_detail, name='detail'),
]