from django.shortcuts import get_object_or_404, render
from .serializers import CardSerializer, OrderSerializer
from .models import Card, Order
from shopApp.models import Product
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = [IsAuthenticated]

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_to_Card(self, request, pk):
        item = get_object_or_404(Product, pk=pk)
        order_item = Card.objects.get_or_create(user=request.user, item=item, purchase=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False).exists()
        if order_qs:
            order = order_qs.first()
            if order.order_items.filter(item=item).exists():
                order_item.quantity += 1
                order_item.save()
                return Response({"message": "Item added to Card"}, status=status.HTTP_200_OK)
            else:
                order.orderItems.add(order_item[0])
                return Response({"message": "Item added to Card"}, status=status.HTTP_200_OK)
        else:
            order = Order.objects.create(user=request.user)
            order.orderItems.add(order_item[0])
            return Response({"message": "Item added to Card"}, status=status.HTTP_200_OK)



    

