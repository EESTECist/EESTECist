from django.shortcuts import render, get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .serializers import UserSerializer, CategorySerializer, PostSerializer, NotificationSerializer
from forum.models import Post, Category, Permission

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(username = username, password = password)

        if not user:
            return Response({'error': 'username or password is incorrect!'})

        token, _ = Token.objects.get_or_create(user = user)

        return Response({'token': token.key, 'user_id': user.id})

    return Response({'error': 'do not send empty requests!'})

class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, TokenAuthentication)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        profile_serializer = self.get_serializer(instance)
        logged_in_serializer= self.get_serializer(request.user)
        post_serializer = PostSerializer(instance.post_set.all(), many = True)

        data = {
            'logged_in_user': logged_in_serializer.data,
            'profile_user': profile_serializer.data,
            'posts': post_serializer.data,
        }

        return Response(data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, TokenAuthentication)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        data = {}

        for query in queryset:
            data[query.id] = CategorySerializer(query).data
            if len(query.post_set.all()) > 0:
                data['{}-latest-post'.format(query.id)] = PostSerializer(query.post_set.latest()).data

        return Response(data)

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, TokenAuthentication)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        category_serializer = self.get_serializer(instance)
        post_serializer = PostSerializer(instance.post_set.all(), many = True)

        return Response({'category': category_serializer.data, 'posts': post_serializer.data})

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, TokenAuthentication)

class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (SessionAuthentication, TokenAuthentication)

@api_view(['POST'])
@authentication_classes((SessionAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated, ))
def set_permission(request):
    logged_in_user_permission = Permission.objects.get(user = request.user)
    if logged_in_user_permission.is_mod:

        other_user = request.data.get('user')
        permissions = Permission.objects.get(user = other_user)
        permissions.update(**requst.data)
        permissions.save()

    return Response({'error': 'Unauthorized attempt'}, status = HTTP_401_UNAUTHORIZED)

class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(user = get_object_or_404(User, id = kwargs['pk']))
        serializer = self.get_serializer(queryset, many = True)

        return Response(serializer.data)
