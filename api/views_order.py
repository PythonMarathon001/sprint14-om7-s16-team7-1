from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from order.models import Order
from .serializer import OrderSerializer


class ApiOrders(APIView):
    def get(self, request):
        all_orders = Order.objects.all()
        serializer = OrderSerializer(all_orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiOrderPK(APIView):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, pk):
        if Order.delete_by_id(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        order = Order.objects.get(pk=pk)
        data = request.data
        serializer = OrderSerializer(instance=order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(f"Successful updated {order}", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
