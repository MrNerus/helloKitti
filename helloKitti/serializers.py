from rest_framework import serializers
from .models import Blogs, Users, Comments, Likes, CommentLikes, Testimonials

class BlogsSerializer(serializers.ModelSerializer):
    imgPath = serializers.SerializerMethodField()
    class Meta:
        model = Blogs
        fields = "__all__"

    def get_imgPath(self, obj):
        request = self.context.get('request')
        imgPath = "/helloKitti" + obj.imgPath
        return request.build_absolute_uri(imgPath)
    
    # To look at: hyperlink model serializer

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"

class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLikes
        fields = "__all__"

class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = "__all__"