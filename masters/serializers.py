from rest_framework import serializers
from .models import MasterModel, OrderModel


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterModel
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('__all__')
