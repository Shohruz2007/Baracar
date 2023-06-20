from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

import string
import random

from baracar.permissions import IsAdminUserOrReadOnly
from .serializers import *
from .models import *


class UzModelAPIView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = UzModelSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuModelAPIView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = RuModelSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ModelChangeAPIView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = ModelChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SeriesChangeAPIView(viewsets.ModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = SeriesChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzSeriesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = UzSeriesSerializer
    permission_classes = [AllowAny]

class RuSeriesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = RuSeriesSerializer
    permission_classes = [AllowAny]


class UzPositionAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = UzPositionSerializer
    permission_classes = [AllowAny]

class RuPositionAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = RuPositionSerializer
    permission_classes = [AllowAny]

class PositionChangeAPIView(viewsets.ModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = PositionChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzFuelSortAPIView(viewsets.ModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = UzFuelSortSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuFuelSortAPIView(viewsets.ModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = RuFuelSortSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzGearBoxAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = UzGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuGearBoxAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = RuGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class UzGearBoxAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = UzGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuGearBoxAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = RuGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzGarantAPIView(viewsets.ModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = UzGarantSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuGarantAPIView(viewsets.ModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = RuGarantSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzEnginePlaceAPIView(viewsets.ModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = UzEnginePlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuEnginePlaceAPIView(viewsets.ModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = RuEnginePlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzBranchAPIView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = UzBranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuBranchAPIView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = RuBranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzOrderAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = UzOrderSerializer
    permission_classes = [IsAuthenticated]

class RuOrderAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = RuOrderSerializer
    permission_classes = [IsAuthenticated]


class OrderChangeAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderChangeSerializer
    permission_classes = [IsAuthenticated]


class ImageAPIView(viewsets.ModelViewSet):
    queryset = CarImages.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def rename_image(self, data):
        total = string.ascii_letters  # getting random name for image
        generated_name = "".join(random.sample(total, 15))  
        
        data_copy = data.copy()
        image_format = data_copy['image'].name.split('.')[-1]  #getting the format type of image
        data_copy['image'].name = f'{generated_name}.{image_format}'
        return data_copy
    
    
    def create(self, request, *args, **kwargs):  # limit image size
        if request.data["image"].size > 5 * 1024 * 1024:
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        
        changed_data = self.rename_image(request.data)
        
        serializer = self.get_serializer(data=changed_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        
        changed_data = self.rename_image(request.data)
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=changed_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class UzCarAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = UzCarSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs.get("pk")
        car = Car.objects.get(pk=pk)  # counting views
        car.views += 1
        car.save()
        return Response(serializer.data)

class RuCarAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = RuCarSerializer

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


class UzDefectAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = UzDefectSerializer

class RuDefectAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = RuDefectSerializer


class DefectChangeAPIView(viewsets.ModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = DefectChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def rename_image(self, data):
        def generate_name():
            total = string.ascii_letters  # getting random name for image
            generated_name = "".join(random.sample(total, 15))
            return generated_name
        
        data_copy = data.copy()
        image1_format = data_copy['image1'].name.split('.')[-1]  #getting the format type of image
        image2_format = data_copy['image2'].name.split('.')[-1]  #getting the format type of image
        

        data_copy['image1'].name = f'{generate_name()}.{image1_format}'
        data_copy['image2'].name = f'{generate_name()}.{image2_format}'
        return data_copy
    
    def create(self, request, *args, **kwargs):  # limit image size
        if (
            request.data["image1"].size
            and request.data["image2"].size > 5 * 1024 * 1024
        ):
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        
        changed_data = self.rename_image(request.data)

        
        serializer = self.get_serializer(data=changed_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        
        changed_data = self.rename_image(request.data)
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=changed_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]

class BlankAPIView(viewsets.ModelViewSet):
    serializer_class = BlankSerializer
    queryset = Blank.objects.all()
    permission_classes = [IsAdminUser]
