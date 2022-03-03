from . import views
from django.urls import path

urlpatterns = [
    path('',views.getData),
    path('item/<str:pk>/',views.getSingleData, name="item"),
    path('create/',views.postData, name="create"),
    path('update/<str:pk>/',views.updateData, name="update"),
    path('delete/<str:pk>/',views.deleteData, name="delete"),
]
intentiona error