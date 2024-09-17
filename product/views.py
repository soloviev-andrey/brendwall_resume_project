from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Проверки перед созданием продукта
        if serializer.validated_data['price'] <= 0:
            raise serializers.ValidationError("Цена должна быть положительным числом.")
        serializer.save()
