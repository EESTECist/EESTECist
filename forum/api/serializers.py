from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from forum.models import Permission, Notification, Category, Post, Follower

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        try:
            new_user = User.objects.create_user(username = username, password = password)
        except IntegrityError:
            return None

        return new_user

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('user', 'name', 'date')

    def create(self, validated_data):
        user = get_object_or_404(User, username = validated_data['user'])
        name = validated_data['name']

        new_category = Category(user = user, name = name)
        new_category.save()

        return new_category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'anon', 'date', 'text', 'category', 'vote', 'media')

    def create(self, validated_data):
        user = get_object_or_404(User, username = validated_data['user'])
        category = get_object_or_404(Category, name = validated_data['category'])
        anon = validated_data['anon']
        text = validated_data['text']

        if validated_data.get('media'):
            media = validated_data['media']

            new_post = Post(user = user, category = category, media = media, anon = anon, text = text)
            new_post.save()

        new_post = Post(user = user, category = category, anon = anon, text = text)
        new_post.save()

        return new_post

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    _from = UserSerializer()
    class Meta:
        model = Notification
        fields = ('user', '_from', 'text', 'date')

class FollowerSerializer(serializers.ModelSerializer):
    follower = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Follower
        fields = ('category', 'follower')

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('user', 'is_mod', 'time_of_restriction', 'banned', 'can_create', 'can_vote')
