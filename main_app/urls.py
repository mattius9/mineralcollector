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
    path('minerals/<int:mineral_id>/add_viewing/', views.add_viewing, name='add_viewing'),
    path('minerals/<int:mineral_id>/assoc_tool/<int:tool_id>', views.assoc_tool, name='assoc_tool'),
    path('minerals/<int:mineral_id>/unassoc_tool/<int:tool_id>', views.unassoc_tool, name='unassoc_tool'),
    path('tools/', views.ToolList.as_view(), name='tools_index'),
    path('tools/<int:pk>/', views.ToolDetail.as_view(), name='tools_detail'),
    path('tools/create/', views.ToolCreate.as_view(), name='tools_create'),
    path('tools/<int:pk>/update/', views.ToolUpdate.as_view(), name='tools_update'),
    path('tools/<int:pk>/delete/', views.ToolDelete.as_view(), name='tools_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]