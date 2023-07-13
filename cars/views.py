from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.settings import api_settings

import string
import random
from copy import deepcopy, copy

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
    queryset = CarSeries.objects.select_related('model').all()
    serializer_class = UzSeriesSerializer
    permission_classes = [AllowAny]
    
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RuSeriesAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarSeries.objects.select_related('model').all()
    serializer_class = RuSeriesSerializer
    permission_classes = [AllowAny]


class UzPositionAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarPosition.objects.select_related('series').select_related('series__model').all()
    serializer_class = UzPositionSerializer
    permission_classes = [AllowAny]

class RuPositionAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarPosition.objects.select_related('series').select_related('series__model').all()
    serializer_class = RuPositionSerializer
    permission_classes = [AllowAny]

class PositionChangeAPIView(viewsets.ModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = PositionChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzFuelSortAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = UzFuelSortSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuFuelSortAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = RuFuelSortSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class FuelSortChangeAPIView(viewsets.ModelViewSet):
    queryset = CarFuelSort.objects.all()
    serializer_class = FuelSortChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzGearBoxAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = UzGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuGearBoxAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = RuGearBoxSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class GearBoxChangeAPIView(viewsets.ModelViewSet):
    queryset = CarGearbox.objects.all()
    serializer_class = GearBoxChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzGarantAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = UzGarantSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuGarantAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = RuGarantSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class GarantChangeAPIView(viewsets.ModelViewSet):
    queryset = CarGarantType.objects.all()
    serializer_class = GarantChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzEnginePlaceAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = UzEnginePlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuEnginePlaceAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = RuEnginePlaceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EnginePlaceChangeAPIView(viewsets.ModelViewSet):
    queryset = CarEnginePlace.objects.all()
    serializer_class = EnginePlaceChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzBranchAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = UzBranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class RuBranchAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = RuBranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class BranchChangeAPIView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchChangeSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzOrderAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.select_related('user').select_related('car').select_related('branch').all()
    serializer_class = OrderGetSerializer
    permission_classes = [IsAuthenticated]

class RuOrderAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.select_related('user').select_related('car').select_related('branch').all()
    serializer_class = OrderGetSerializer
    permission_classes = [IsAuthenticated]


class OrderChangeAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderChangeSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return OrderGetSerializer
        return OrderChangeSerializer
    

    
class ImageAPIView(viewsets.ModelViewSet):
    queryset = CarImages.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def rename_image(self, data):
        total = string.ascii_letters  # getting random name for image
        generated_name = "".join(random.sample(total, 15))  

        image_from_request = data['image']
        car_id_from_request = data['car']
        
        image_format = image_from_request.name.split('.')[-1]  #getting the format type of image
        image_from_request.name = f'{generated_name}.{image_format}'
        
        new_data = {'image':image_from_request,'car':car_id_from_request}
        return new_data
    
    
    def create(self, request, *args, **kwargs):  # limit image size

        if "image" in request.data:
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
        return Response({'error':"image doestn't exist so plese enter an image type of jpeg, jpg or img"}, status=status.HTTP_204_NO_CONTENT)
    
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
    queryset = Car.objects.select_related('garant').select_related('position').select_related('fuel_sort').select_related('branch').select_related('engine_place').select_related('position__series').select_related('position__series__model').select_related('gearbox').all()
    serializer_class = UzCarSerializer

    
    def list(self, request, *args, **kwargs):
        if 'currency_reload' in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            for car_obj in queryset:
                car_obj.set_actual_currency()

        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs.get("pk")
        car = Car.objects.get(pk=pk)  # counting views
        car.views += 1
        car.save()
        return Response(serializer.data)

class RuCarAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.select_related('garant').select_related('position').select_related('fuel_sort').select_related('branch').select_related('engine_place').select_related('position__series').select_related('position__series__model').select_related('gearbox').all()
    serializer_class = RuCarSerializer

    
    def list(self, request, *args, **kwargs):
        if 'currency_reload' in request.query_params:
            queryset = self.filter_queryset(self.get_queryset())
            for car_obj in queryset:
                car_obj.set_actual_currency()

        queryset = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
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
    # permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        data = serializer.save()
        data.set_actual_currency()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    
class CarHistoryAPIView(viewsets.ModelViewSet):
    queryset = CarHistory.objects.all()
    serializer_class = CarHistorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class UzDefectAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarDefect.objects.select_related('car').all()
    serializer_class = UzDefectSerializer

class RuDefectAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CarDefect.objects.select_related('car').all()
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
        
        image_from_request1 = data['image1']
        image_from_request2 = data['image2']
        uz_description_from_request = data['description_uz']
        ru_description_from_request = data['description_ru']
        car_id_from_request = data['car']

        
        image1_format = image_from_request1.name.split('.')[-1]  #getting the format type of image
        image2_format = image_from_request2.name.split('.')[-1]  #getting the format type of image
        

        image_from_request1.name = f'{generate_name()}.{image1_format}'
        image_from_request2.name = f'{generate_name()}.{image2_format}'
        
        
        
        new_data = {'image1':image_from_request1,'image2':image_from_request2,'description_uz':uz_description_from_request,'description_ru':ru_description_from_request,'car':car_id_from_request}

        return new_data
    
    def create(self, request, *args, **kwargs):  # limit image size
        if 'image1' and 'image2' in request.data:
            if (request.data["image1"].size or request.data["image2"].size) > 5 * 1024 * 1024:
                return Response({'error':"image size is too large, it must be no more than 5Mb!"},status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)
        
            changed_data = self.rename_image(request.data)

            
            serializer = self.get_serializer(data=changed_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response({'error':"image doestn't exist. Plese enter images type of jpeg, jpg or img"}, status=status.HTTP_204_NO_CONTENT)

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

class CallToUserAPIView(viewsets.ModelViewSet):
    serializer_class = CallToUserSerializer
    queryset = CallToUser.objects.all()

class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]

class BlankAPIView(viewsets.ModelViewSet):
    serializer_class = BlankSerializer
    queryset = Blank.objects.all()
    permission_classes = [IsAdminUser]
