from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    
    name = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    image = serializers.ImageField(read_only=True)
    