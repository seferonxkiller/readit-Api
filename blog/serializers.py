from rest_framework import serializers
from .models import Category, Tag, Article, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticleGetSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.title', read_only=True)
    category = CategorySerializer(required=False)
    tags = TagSerializer(required=True, many=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'created_date']


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']
