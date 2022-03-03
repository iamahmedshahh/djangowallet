# djangowallet

This is a Django REST API example with wallets as a model. I have created a wallet app inside the djangowallet/ project.

This wallet app has a model called wallet. (Go to models.py file)

This model has a field called "rddresss" (Walet is the class name for models.py)

I have defined CRUD functions inside views.py (default)

I am also using serializers, refer to serializers.py file (Targets our Wallet model, which is model.py file and we have a single field called ```raddress```)

Our views.py file contains all of our CRUD methods, we have added an additional get method that displays all of our URLs in the base function

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





