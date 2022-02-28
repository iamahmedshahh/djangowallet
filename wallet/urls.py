from django.urls import path
from . import views


urlpatterns = [
    path('', views.getData),
    path('item/<str:pk>/', views.getSingleData, name="item"),
    path('create/', views.postData, name="create"),
]