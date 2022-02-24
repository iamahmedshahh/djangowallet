from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WalletSerializer
from .models import Wallet

@api_view(['GET'])
def getData(request):
    queryset = Wallet.objects.all()
    serializer = WalletSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

