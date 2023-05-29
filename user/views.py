import vonage
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model, authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from baracar.permissions import IsAdminUserOrReadOnly


from .models import CustomUser, Adress
from .serializers import RegistrationSerializer, UserSerializer, LoginSerializer, AdressSerializer


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



            # client = vonage.Client(key="36c0b7f0", secret="PuT19VQxc6sQYNLn")
            # sms = vonage.Sms(client)
            # responseData = sms.send_message(
            #     {
            #         "from": "Vonage APIs",
            #         "to": "998900325312",
            #         "text": "Test message",
            #     }
            # )
            # if responseData["messages"][0]["status"] == "0":
            #     print("Message sent successfully.")
            # else:
            #     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")



            return Response(self.get_tokens_for_user(user), status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
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

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return {'refresh': str(refresh), 'access': str(refresh.access_token), 'is_staff':user.is_staff}

class AdminUserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdminUser]

class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    http_method_names = ['get', 'put']
    permission_classes = [IsAuthenticated]


class AdressAPIView(viewsets.ModelViewSet):
    serializer_class = AdressSerializer
    queryset = Adress.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
