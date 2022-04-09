from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from authentication.models import CustomUser
from order.models import Order
from .serializer import CustomUserSerializer
from .serializer import OrderSerializer


class ApiCustomUser(APIView):
    def get(self, request):
        all_users = CustomUser.objects.all()
        serializer = CustomUserSerializer(all_users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiCustomUserPK(APIView):
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        if CustomUser.delete_by_id(pk):
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        data = request.data
        serializer = CustomUserSerializer(instance=user, data=data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response(f"Successful updated {user}", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ApiUserOrderPK(APIView):
    def get(self, request, user_pk, order_pk):
        order = get_object_or_404(Order, pk=order_pk)
        if order.user.id != user_pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def patch(self, request, user_pk, order_pk):
        order = get_object_or_404(Order, pk=order_pk)
        if order.user.id != user_pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = OrderSerializer(instance=order, data=data, partial=True)
        if serializer.is_valid():
            order = serializer.save()
            return Response(f"Successful updated {order}", status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_pk, order_pk):
        order = get_object_or_404(Order, pk=order_pk)
        if order.user.id != user_pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Order.delete_by_id(order_pk)
        return Response(status=status.HTTP_200_OK)
