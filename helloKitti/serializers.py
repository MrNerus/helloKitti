from rest_framework import serializers
# from .models import Blogs, Users, Comments, Testimonials
from .models import Blogs, Users, Comments, Likes, CommentLikes, Testimonials

# class BlogsSerializer(serializers.ModelSerializer):
#     imgPath = serializers.SerializerMethodField()
#     content = serializers.SerializerMethodField()
#     class Meta:
#         model = Blogs
#         fields = "__all__"

#     def get_imgPath(self, obj):
#         request = self.context.get('request')
#         imgPath = "/helloKitti" + obj.imgPath
#         return request.build_absolute_uri(imgPath)
    
#     def get_content(self, obj):
#         return f"{obj.content[:500]}..." if len(obj.content) > 500 else obj.content

class BlogsSerializer(serializers.ModelSerializer):
    imgPath = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    # comments = serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = ['title', 'author', 'content', 'imgPath', 'created_at', 'likes_count', 'comments_count']

    # Define method to get likes_count
    def get_likes_count(self, obj):
        return obj.likes.count()

    # Define method to get comments_count
    def get_comments_count(self, obj):
        return obj.comments.count()

    # Define method to get comments
    # def get_comments(self, obj):
    #     comments = obj.comments.all()
    #     return CommentsSerializer(comments, many=True).data
    
    def get_imgPath(self, obj):
        request = self.context.get('request')
        imgPath = "/helloKitti" + obj.imgPath
        return request.build_absolute_uri(imgPath)
    
    def get_content(self, obj):
        return f"{obj.content[:500]}..." if len(obj.content) > 500 else obj.content
    

class BlogSerializer(serializers.ModelSerializer):
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
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = Testimonials
        fields = "__all__"
    
    def get_avatar(self, obj):
        request = self.context.get('request')
        avatar = "/helloKitti" + obj.avatar
        return request.build_absolute_uri(avatar)