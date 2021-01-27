from django.urls import path

from . import views

app_name = 'manager_url'
urlpatterns = [
    path('', views.manager_list_view, name='manager_list_view'),
    path('<int:pk>/', views.manager_detail_view, name='manager_detail_view'),
    path('create/', views.manager_create_view, name='manager_create_view'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),

    path('<int:pk>/delete', views.manager_delete_view, name='manager_delete_view'),
    path('<int:pk>/change/', views.ManagerUpdate.as_view(), name='ManagerUpdate')
]