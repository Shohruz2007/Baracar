from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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


            # from twilio.rest import Client  #sms message sending via twilio
            #
            # account_sid = ''
            # auth_token = ''
            # client = Client(account_sid, auth_token)
            #
            # message = client.messages.create(
            #     from_='',
            #     body=f"{serializer.data['verify_code']}",
            #     to=''
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
        return {'refresh': str(refresh), 'access': str(refresh.access_token), 'is_staff':user.is_staff}


class ChangePasswordView(UpdateAPIView):
        serializer_class = ChangePasswordSerializer
        model = CustomUser
        # permission_classes = (IsAuthenticated,)

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


class AdressAPIView(viewsets.ModelViewSet):
    serializer_class = AdressSerializer
    queryset = Adress.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]  # from custom permission checking admin
