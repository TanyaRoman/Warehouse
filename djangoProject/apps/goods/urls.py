from django.urls import path

from . import views

app_name = 'goods_url'
urlpatterns = [
    path('', views.goods_list_view, name='goods_list_view'),
    path('<int:pk>/', views.goods_detail_view, name='goods_detail_view'),
    path('create/', views.goods_create_view, name='goods_create_view'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),

    path('<int:pk>/delete', views.goods_delete_view, name='goods_delete_view'),
    # path('<int:pk>/change/', views.goods_change_view, name='goods_change_view')
    path('<int:pk>/change/', views.GoodsUpdate.as_view(), name='GoodsUpdate')
]