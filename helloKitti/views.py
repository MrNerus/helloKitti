from django.shortcuts import render
from . serializers import BlogsSerializer, BlogSerializer, TestimonialsSerializer
from . models import Blogs, Testimonials
from rest_framework import generics

from django.shortcuts import get_object_or_404
from django.http import FileResponse


# Create your views here.
def test(request):
    pass


# To get all blogs
class API_getBlogs(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

# To get exactly one required blog
class API_getBlog(generics.RetrieveAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'

# To get n number of blogs
class API_getNBlogs(generics.ListAPIView):
    serializer_class = BlogsSerializer
    def get_queryset(self):
        numberOfPost = self.kwargs['numberOfPost']
        return Blogs.objects.order_by('-created_at')[:numberOfPost]

# To get all Testimonials
class API_getTestimonials(generics.ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer

# To get exactly one required Testimonial
class API_getTestimonial(generics.RetrieveAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    lookup_field = 'id'

# To get n number of Testimonials
class API_getNTestimonials(generics.ListAPIView):
    serializer_class = TestimonialsSerializer
    def get_queryset(self):
        numberOfTestimonials = self.kwargs['numberOfTestimonials']
        return Testimonials.objects.order_by('-said_at')[:numberOfTestimonials]


def get_image(request, img):
    image_path = f'helloKitti/media/BlogImages/{img}'
    return FileResponse(open(image_path, 'rb'))

def get_avatar(request, img):
    image_path = f'helloKitti/media/avatar/{img}'
    return FileResponse(open(image_path, 'rb'))