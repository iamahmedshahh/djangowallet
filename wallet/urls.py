from django.urls import path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.getData),
    path('item/<str:pk>/', views.getSingleData, name="item"),
    path('create/', views.postData, name="create"),

]