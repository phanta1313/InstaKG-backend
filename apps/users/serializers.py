from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.username')

    class Meta:
        model = Post
        fields = ("image", "text", "likes", "owner")


class PostCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("image", "text")

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

