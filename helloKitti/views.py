from django.shortcuts import render
from . serializers import BlogsSerializer
from . models import Blogs
from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.http import FileResponse


# Create your views here.
def test(request):
    pass

class API_getBlogs(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

class API_getBlog(generics.RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer
    lookup_field = 'id'

class API_getNBlogs(generics.ListAPIView):
    serializer_class = BlogsSerializer
    def get_queryset(self):
        numberOfPost = self.kwargs['numberOfPost']
        return Blogs.objects.order_by('-created_at')[:numberOfPost]


def get_image(request, img):
    image_path = f'helloKitti/media/BlogImages/{img}'
    return FileResponse(open(image_path, 'rb'))