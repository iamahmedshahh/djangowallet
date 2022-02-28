from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import WalletSerializer
from .models import Wallet


@api_view(['GET'])
def getData(request):
    queryset = Wallet.objects.all()
    serializer = WalletSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def getSingleData(request,pk):
    queryset = Wallet.objects.all(id=pk)
    serializer = WalletSerializer(queryset, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = WalletSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)