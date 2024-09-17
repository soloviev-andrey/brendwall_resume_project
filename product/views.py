from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render


def index(request):
    return render(request, 'product/index.html')


class ProductListCreateView(generics.ListCreateAPIView):
    """Представление для получения списка продуктов и создания нового продукта."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Сохраняет новый продукт после валидации."""
        serializer.save()
