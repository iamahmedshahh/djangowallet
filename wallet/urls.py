from . import views
from django.urls import path

urlpatterns = [
    path('', views.getUrls),
    path('wallet/',views.getData),
    path('wallet/<str:pk>/',views.getSingleData, name="wallet"),
    path('create/',views.postData, name="create"),
    path('update/<str:pk>/',views.updateData, name="update"),
    path('delete/<str:pk>/',views.deleteData, name="delete"),
]