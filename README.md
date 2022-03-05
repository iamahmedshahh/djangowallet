# djangowallet

First of All credits to https://github.com/GuillaumeFalourd For Helping out with the PyTest Action

This is a Django REST API example with wallets as a use-case. 
I have created a Wallet API inside the djangowallet/ project.
Start by creating a new Django Project from the Command.


```
django-admin createproject djangowallet 

#instead of python you can use py or pip, anything that works for you
```

This command created a project called djangowallet. To create our Actual REST API we will run another command within the root of our project

```
python startapp wallet  
```

The command above created our actual api called wallet. This is our Django REST API that will give the neccessary files to create a Rest API. Run the following commands to save your work after creating the API.

```
python manage.py makemigrations
python manage.py migrate
```

# Base Level Settings #

Go to your settings.py file in the Root directory of djangowallet and add the following under ```Installed_APPS = ``` paranthesis

```
BEFORE

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


AFTER

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wallet',
    'rest_framework',
]

```

We can always Add multiple api's in our root django project, so we have to navigate our base project to whatever API we want to work with. The ```rest_framework``` here is a prerequisite when working with API's. Run command #23, #24.

We have to navigate our BASE project to work with the URLs we will create in our API to do this look for ```djangowallet/urls.py```


# Navigating our API URLS to Project URLS with djangowallet/URLS.PY #

```
BEFORE

urlpatterns = [
    path('admin/', admin.site.urls),
]

AFTER

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wallet.urls'))
]
```

We have added another PATH where the project will look for the URLS in our APP/API URLs. Note, we have a urls.py file in our API folder as well. We are all set and done now we can work with our API


# WORKING WITH THE API #

This wallet api has a model.py file and inside that our model class name wallet the same name as our API (Not Obligatory). We have a single field called ```raddress```. 

These are the fields that we will get, post, update or delete. These are our keys in a key, value relationship

# Creating our data fields with models.py #

```
from django.db import models

class Wallet(models.Model):
    raddress = models.CharField(max_length=60)
    ### ADD more fields here ###

    def __str__(self):
        return self.name
```

Let's create a serializer. 
```Serialziers things are absolutely neccessary to make sure there is no DATA TYPE mix up, serializers convert python data types to JSON and De-Serializers do the opposite```.
 
Start by creating a serializers.py file. 
Creating a serializers is not hard at all as Django REST framework provides us with.
Model serializer function this will automatically serialize all our fields in the models.py file. 
We don't have a serializers file by default in our API. 
Create a serialzers.py file under the wallet directory and not the root directory

# Serialization with Serializers.PY

```
from rest_framework import serializers

from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')
```



The most important is our views.py file that contains all of our CRUD methods I have added an additional GET method that displays all of our URLs in the base function

# Creating CRUD functions with Views.py


```
@api_view(['GET'])
def getUrls(request):
    api_urls = {
        'Wallets': '/wallet',k
        'items': 'item/<str:pk>/',
        'create': '/create',
        'Update': '/update/pk',
        'Delete': 'delete/<str:pk>/'
    }
  
    return Response(api_urls)
```

This is the response we will get in our front-end


```
HTTP 200 OK
Allow: GET, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Wallets": "/wallet",
    "items": "item/<str:pk>/",
    "create": "/create",
    "Update": "/update/pk",
    "Delete": "delete/<str:pk>/"
}
```

# Getting All DATA

```
@api_view(['GET'])
def getData(request):
    queryset = Wallet.objects.all()
    serializer = WalletSerializer(queryset,many=True,context={'request': request})
    return Response(serializer.data)
```

Returns all of the key value data.

``` django rest api adds and ID key default. The value of id is incremental by default```


# Getting Filtered Data

```
@api_view(['GET'])
def getSingleData(request,pk):
    queryset = Wallet.objects.get(id=pk)
    serializer = WalletSerializer(queryset,many=False)
    return Response(serializer.data)
```

``` We have added another parameter (PK) which is the private key. In the function above ID is the private key here. A user will add /id and the api will filter the posts with only the given id or any other key ```

There is also a URLs.py file within the API directory. This is the file which will contain all the URL patterns for the API.

# Creating URL endpoints with Urls.py
```

from . import views
from django.urls import path

urlpatterns = [
    path('', views.getUrls),
    path('wallet/',views.getData),
    path('item/<str:pk>/',views.getSingleData, name="item"),
    path('create/',views.postData, name="create"),
    path('update/<str:pk>/',views.updateData, name="update"),
    path('delete/<str:pk>/',views.deleteData, name="delete"),
]
```

``` <str:pk> will be the id or the key you want to filter data from ```

# Run the API

``` python manage.py runserver ```

The command above will start the localhost django api framework. Navigate to 127.0.0.1:8000

In my project I have the following URLS

```
127.0.0.1:8000/wallet/
127.0.0.1:8000/item/id
127.0.0.1:8000/create/
127.0.0.1:8000/update/id
127.0.0.1:8000/delete/id
```




