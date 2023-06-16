from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

import string
import random

from baracar.permissions import IsAdminUserOrReadOnly
from .serializers import *
from .models import *


class ModelAPIView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SeriesChangeAPIView(viewsets.ModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = SeriesChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SeriesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = SeriesSerializer


class PositionAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = PositionSerializer


class PositionChangeAPIView(viewsets.ModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = PositionChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class FuelSortAPIView(viewsets.ModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = FuelSortSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class GearBoxAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = GearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class GarantAPIView(viewsets.ModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = GarantSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EnginePlaceAPIView(viewsets.ModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = EnginePlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BranchAPIView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class OrderAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = IsAuthenticated


class OrderChangeAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderChangeSerializer
    permission_classes = IsAuthenticated


class ImageAPIView(viewsets.ModelViewSet):
    queryset = CarImages.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):  # limit image size
        if request.data["image"].size > 5 * 1024 * 1024:
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        

        total = string.ascii_letters  # getting random name for image
        generated_name = "".join(random.sample(total, 15))  
        
        data_copy = request.data.copy()
        image_format = data_copy['image'].name.split('.')[-1]  #getting the format type of image
        data_copy['image'].name = f'{generated_name}.{image_format}'
        
        serializer = self.get_serializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class CarAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs.get("pk")
        car = Car.objects.get(pk=pk)  # counting views
        car.views += 1
        car.save()
        return Response(serializer.data)


class CarChangeAPIView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CarHistoryAPIView(viewsets.ModelViewSet):
    queryset = CarHistory.objects.all()
    serializer_class = CarHistorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class DefectAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = DefectSerializer


class DefectChangeAPIView(viewsets.ModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = DefectChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):  # limit image size
        if (
            request.data["image1"].size
            and request.data["image2"].size > 5 * 1024 * 1024
        ):
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

        def generate_name():
            total = string.ascii_letters  # getting random name for image
            generated_name = "".join(random.sample(total, 15))
            return generated_name
        
        data_copy = request.data.copy()
        image1_format = data_copy['image1'].name.split('.')[-1]  #getting the format type of image
        image2_format = data_copy['image2'].name.split('.')[-1]  #getting the format type of image
        

        data_copy['image1'].name = f'{generate_name()}.{image1_format}'
        data_copy['image1'].name = f'{generate_name()}.{image2_format}'
        
        serializer = self.get_serializer(data=data_copy)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]
