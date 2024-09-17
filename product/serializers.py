from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        """Проверка, что цена должна быть положительным числом."""
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть положительным числом.")
        return value
