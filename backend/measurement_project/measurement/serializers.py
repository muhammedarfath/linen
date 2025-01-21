from rest_framework import serializers
from accounts.models import CommonOrderDetails, Shirt, Pant,WomensOrderDetails

class CommonOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonOrderDetails
        fields = '__all__'

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = '__all__'

class PantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pant
        fields = '__all__'
        
class WomensOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomensOrderDetails
        fields = '__all__'                
