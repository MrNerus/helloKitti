from django.urls import path
from . import views as kittyView
from .views import API_getBlogs, API_getBlog, API_getNBlogs
from .views import API_getTestimonials, API_getTestimonial, API_getNTestimonials

urlpatterns = [
    path('api/blogs/', API_getBlogs.as_view()),
    path('api/blogs/all/', API_getBlogs.as_view()),
    path('api/blog/<int:id>', API_getBlog.as_view()),
    path('api/blogs/<int:numberOfPost>', API_getNBlogs.as_view()),

    path('api/testimonials/', API_getTestimonials.as_view()),
    path('api/testimonials/all/', API_getTestimonials.as_view()),
    path('api/testimonial/<int:id>', API_getTestimonial.as_view()),
    path('api/testimonials/<int:numberOfTestimonials>', API_getNTestimonials.as_view()),
    
    path('media/BlogImages/<str:img>', kittyView.get_image),
    path('media/avatar/<str:img>', kittyView.get_avatar),
]