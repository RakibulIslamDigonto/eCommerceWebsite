from django.shortcuts import render, redirect
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from django.db.models import Q
import datetime
from .models import Product, Category
from loginApp.models import User
from .serializers import CategorySerializer, ProductSerializer


# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        data['created_by'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer = serializer.save()
            # Category.objects.create(category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        category=Category.objects.filter(pk=pk).exists()
        if category:
            category = Category.objects.get(pk=pk)
            serializer = self.serializer_class(category, data=request.data)
            if serializer.is_valid():
                serializer = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    def details(self, request, pk):
        category = Category.objects.filter(pk=pk).exists()
        if category:
            category = Category.objects.get(pk=pk)
            serializer = self.serializer_class(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        category = Category.objects.filter(pk=pk).exists()
        if category:
            category = Category.objects.get(pk=pk).delete()
            return Response({"message": "Category deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions = [permissions.IsAuthenticated]

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        data['created_by'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid:
            serializer = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        product = Product.objects.filter(pk=pk).exists()
        if product:
            product = Product.objects.get(pk=pk)
            serializer = self.serializer_class(product, data=request.data)
            if serializer.is_valid():
                serializer = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def details(self, request, pk):
        product = Product.objects.filter(pk=pk).exists()
        if product:
            product = Product.objects.get(pk=pk)
            serializer = self.serializer_class(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        product = Product.objects.filter(pk=pk).exists()
        if product:
            product = Product.objects.get(pk=pk).delete()
            return Response({"message": "Product deleted"}, status=status.HTTP_200_OK)
        return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)



