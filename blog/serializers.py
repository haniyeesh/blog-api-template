from rest_framework import serializers
from . models import *
from account.models import User

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field = 'username', queryset = User.objects.all())
    class Meta:
        model = Article
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    class Meta:
        model = Comment 
        fields = ['article','id','name', 'text', 'created_at', 'email', 'parent', 'published', 'replies' ]
        
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many = True).data
        return [] 