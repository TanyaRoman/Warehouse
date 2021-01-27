from django.urls import path

from . import views

app_name = 'purchase_url'
urlpatterns = [
    path('', views.purchase_list_view, name='purchase_list_view'),
    path('<int:pk>/', views.purchase_detail_view, name='purchase_detail_view'),
    path('create/', views.purchase_create_view, name='purchase_create_view'),
    path('back/', views.back, name='back'),
    path('home/', views.home, name='home'),

    path('<int:pk>/delete', views.purchase_delete_view, name='purchase_delete_view'),
    # path('<int:pk>/change/', views.goods_change_view, name='goods_change_view')
    path('<int:pk>/change/', views.PurchaseUpdate.as_view(), name='PurchaseUpdate')
]