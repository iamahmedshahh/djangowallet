from unicodedata import name
from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.getData),
    path('add/<str:pk>/', views.getSingleData, name="add"),
    path('post/', views.postData, name="post"),

]