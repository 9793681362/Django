from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'), # 将根路径与 home 视图函数相关联
    path('api/', views.my_view, name='my_api'),
    path('api/test_data/', views.test_data_api, name='test_data_api'),
]
