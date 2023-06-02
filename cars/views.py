import io
from django.core.files.base import ContentFile
import zipfile
from PIL import Image

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from baracar.permissions import IsAdminUserOrReadOnly
from .serializers import *
from .models import *

class ModelAPIView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SeriesAPIView(viewsets.ModelViewSet):
    queryset = CarSeries.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = SeriesPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class PositionAPIView(viewsets.ModelViewSet):
    queryset = CarPosition.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    def create(self, request, *args, **kwargs):
        serializer = PositionPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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

class BranchAPIView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ImageAPIView(viewsets.ModelViewSet):
    queryset = CarImages.objects.all()
    serializer_class = CarImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.data['folder']:

            z = zipfile.ZipFile(request.data['folder'])
            for i in range(len(z.namelist())):

                file_in_zip = z.namelist()[i]
                if (".jpeg" in file_in_zip or ".JPEG" in file_in_zip):
                    data = z.read(file_in_zip)
                    dataEnc = io.BytesIO(data)
                    print(dataEnc)

                    img = Image.open(dataEnc)
                    img.save("carimg.jpeg")
                    print(img)
                else:
                    return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)



        if request.data['image'].size > 5 * 1024 * 1024:
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class CarAPIView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs.get("pk")
        car = Car.objects.get(pk=pk)
        car.views += 1
        car.save()
        return Response(serializer.data)


    def create(self, request, *args, **kwargs):
        serializer = CarPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DefectImageAPIView(viewsets.ModelViewSet):
    queryset = CarDefectImages.objects.all()
    serializer_class = DefectImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def create(self, request, *args, **kwargs):
        if request.data['image'].size > 5 * 1024 * 1024:
            print(request.data['image'].size)
            return Response(status=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DefectAPIView(viewsets.ModelViewSet):
    queryset = CarDefect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    def create(self, request, *args, **kwargs):
        serializer = DefectPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentAPIView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]