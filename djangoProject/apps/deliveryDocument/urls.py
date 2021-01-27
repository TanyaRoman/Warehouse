from django.urls import path

from . import views

app_name = 'delivery_url'
urlpatterns = [
    path('', views.delivery_list_view, name='delivery_list_view'),
    path('<int:pk>/', views.delivery_detail_view, name='delivery_detail_view'),
    path('create/', views.delivery_create_view, name='delivery_create_view'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),

    path('<int:pk>/delete', views.delivery_delete_view, name='delivery_delete_view'),
    # path('<int:pk>/change/', views.goods_change_view, name='goods_change_view')
    path('<int:pk>/change/', views.DeliveryUpdate.as_view(), name='DeliveryUpdate')
]