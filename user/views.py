import random
import string
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from baracar.permissions import IsAdminUserOrReadOnly


from .models import CustomUser, Adress
from .serializers import *


class RegisterAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


    
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            user = CustomUser(id = data['id'])

            
            
            # from twilio.rest import Client

            # account_sid = 'AC787b403d46cadb54e9690b8ba98fb723'
            # auth_token = '21e3c80e5a1a12e816c9bfaa718a6337'
            # client = Client(account_sid, auth_token)

            # message = client.messages.create(
            # from_='+447782337629',
            # body='1234',
            # to='+998900325312'
            # )

            # print(message.sid)
            

            return Response(self.get_tokens_for_user(user), status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):  # getting JWT tokens
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}



class LoginAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        phone = data.get('phone')
        password = data.get('password')
        user = authenticate(username=phone, password=password)
        if user:
            return Response(self.get_tokens_for_user(user), status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):  # getting JWT token and is_staff boolean
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token), 'is_staff':user.is_staff, 'is_superuser':user.is_superuser}


class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = CustomUser
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    http_method_names = ['get', 'put', 'delete']
    permission_classes = [IsAuthenticated]

    
    def rename_image(self, data):
        total = string.ascii_letters  # getting random name for image
        generated_name = "".join(random.sample(total, 15))  
        
        data_copy = data.copy()
        image_format = data_copy['image'].name.split('.')[-1]  #getting the format type of image
        data_copy['image'].name = f'{generated_name}.{image_format}'
        return data_copy
    
    def update(self, request, *args, **kwargs):
        try: 
            request.data['image']
            update_data = self.rename_image(request.data)
            
        except:
            
            update_data = request.data
            
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=update_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class AdressAPIView(viewsets.ModelViewSet):
    serializer_class = AdressSerializer
    queryset = Adress.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)  
