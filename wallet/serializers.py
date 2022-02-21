from rest_framework import serializers

from .models import Wallet

class WalletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wallet
        fields = ('raddress')