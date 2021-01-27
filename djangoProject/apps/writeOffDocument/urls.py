from django.urls import path

from . import views

app_name = 'write_off_url'
urlpatterns = [
    path('', views.write_off_list_view, name='write_off_list_view'),
    path('<int:pk>/', views.write_off_detail_view, name='write_off_detail_view'),
    path('create/', views.write_off_create_view, name='write_off_create_view'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),

    path('<int:pk>/delete', views.write_off_delete_view, name='write_off_delete_view'),
    # path('<int:pk>/change/', views.goods_change_view, name='goods_change_view')
    path('<int:pk>/change/', views.WriteOffUpdate.as_view(), name='WriteOffUpdate')
]