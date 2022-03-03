# djangowallet

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


WORKING WITH THE API

This wallet api has a model.py file and inside that our model class name wallet the same name as our API (Not Obligatory). We have a single field called ```raddress```. 
These are the fields that we will get, post, update or delete. These are our keys in a key, value relationship

```
from django.db import models

class Wallet(models.Model):
    raddress = models.CharField(max_length=60)

### ADD more if you wish to

    def __str__(self):
        return self.name
```

Let's create a serializer. These things are absolutely neccessary to make sure there is no DATA TYPE mix up. Start by creating a serializers.py file. We don't have a serializers file by default. Create a serialzers.py file under the wallet directory and not the root directory

```
from rest_framework import serializers

from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')
```

Creating a serializers is not hard at all as Django REST framework provides us with .Model serializer function this will automatically serialize all our fields in the models.py file. 


The most important is our views.py file that contains all of our CRUD methods I have added an additional GET method that displays all of our URLs in the base function

```
@api_view(['GET'])
def getUrls(request):
    api_urls = {
        'Wallets': '/wallet',
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





